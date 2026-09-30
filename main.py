from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from gemini_flash import generate_outline

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )


@app.post("/generate")
async def generate(
    request: Request,
    story_prompt: str = Form(...),
    character_name: str = Form(...),
    setting: str = Form(...),
    tone: str = Form(...),
    art_style: str = Form(...)
):
    try:
        outline = generate_outline(
            story_prompt,
            character_name,
            setting,
            tone,
            art_style
        )

        return {
            "status": "success",
            "source": "Gemini",
            "outline": outline
        }

    except Exception:
        outline = []

        for i in range(1, 6):
            outline.append({
                "panel": i,
                "title": f"Panel {i}",
                "scene_description": (
                    f"{character_name} in {setting}. "
                    f"{story_prompt}"
                ),
                "image_prompt": (
                    f"{art_style} style comic panel, "
                    f"{character_name}, {setting}, "
                    f"{tone} mood, panel {i}"
                )
            })

        return {
            "status": "success",
            "source": "Fallback",
            "message": "Gemini quota exceeded. Temporary demo outline used.",
            "outline": outline
        }


@app.get("/test-image")
async def test_image():
    return {
        "status": "success",
        "message": "ComicCraft backend is running"
    }