from __future__ import annotations

import base64
import mimetypes
from pathlib import Path

from langchain_core.messages import HumanMessage
from langchain_ollama.chat_models import ChatOllama


class ImageDescriptionAgent:
    def __init__(self, model: str = "llava:7b", num_ctx: int = 512) -> None:
        self._llm = ChatOllama(model=model, temperature=0, num_ctx=num_ctx)

    def describe_image(self, image_path: str, prompt: str | None = None) -> str:
        path = Path(image_path)
        if not path.exists():
            raise FileNotFoundError(f"Image not found: {image_path}")

        question = prompt or (
            "Descreva esta imagem em detalhes. Cite os principais elementos, "
            "contexto visual, cores predominantes e o que parece estar acontecendo."
        )

        image_b64 = base64.b64encode(path.read_bytes()).decode("utf-8")
        mime_type = mimetypes.guess_type(path.name)[0] or "image/jpeg"

        message = HumanMessage(
            content=[
                {"type": "text", "text": question},
                {"type": "image_url", "image_url": f"data:{mime_type};base64,{image_b64}"},
            ]
        )

        response = self._llm.invoke([message])
        return response.content if isinstance(response.content, str) else str(response.content)
