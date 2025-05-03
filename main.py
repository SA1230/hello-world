from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/invoke")
async def invoke(request: Request):
    data = await request.json()
    fn_name = data.get("tool")
    params = data.get("input", {})

    if fn_name == "say_hello":
        name = params.get("name", "stranger")
        return {"output": f"Hello, {name}!"}
    else:
        return {"error": "Tool not found"}
