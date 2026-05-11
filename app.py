from __future__ import annotations

from pathlib import Path

import streamlit as st

from agent import ImageDescriptionAgent


st.set_page_config(page_title="POC LLaVA Agent", page_icon="🖼️", layout="centered")

st.title("POC: Agente de IA para Descrição de Imagens")
st.caption("LLaVA via Ollama + Orquestração com LangChain + Front em Streamlit")

with st.sidebar:
    st.header("Configuração")
    model_name = st.text_input(
        "Modelo Ollama",
        value="moondream",
        help="Para pouca RAM, prefira moondream ou llava:7b.",
    )
    num_ctx = st.slider("Janela de contexto (num_ctx)", min_value=128, max_value=2048, value=512, step=128)
    custom_prompt = st.text_area(
        "Prompt opcional",
        value=(
            "Descreva esta imagem em detalhes. Fale de objetos, ambiente, "
            "cores e possíveis ações acontecendo na cena."
        ),
    )

uploaded_file = st.file_uploader(
    "Envie uma imagem",
    type=["png", "jpg", "jpeg", "webp"],
    accept_multiple_files=False,
)

if uploaded_file is not None:
    temp_dir = Path("tmp")
    temp_dir.mkdir(exist_ok=True)
    image_path = temp_dir / uploaded_file.name
    image_path.write_bytes(uploaded_file.getbuffer())

    st.image(str(image_path), caption="Imagem enviada", use_container_width=True)

    if st.button("Gerar descrição", type="primary"):
        with st.spinner("Analisando imagem com o modelo vision..."):
            try:
                agent = ImageDescriptionAgent(model=model_name, num_ctx=num_ctx)
                description = agent.describe_image(str(image_path), custom_prompt)
                st.subheader("Descrição gerada")
                st.write(description)
            except Exception as exc:  # noqa: BLE001
                st.error(
                    "Não foi possível gerar a descrição. "
                    "Verifique se o Ollama está rodando e o modelo foi baixado."
                )
                st.exception(exc)
else:
    st.info("Faça upload de uma imagem para começar.")
