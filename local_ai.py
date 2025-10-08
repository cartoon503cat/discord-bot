from llama_cpp import Llama

# Завантаження моделі Phi-2 (локально)
print("🧠 Завантажую модель Phi-2... Це може зайняти кілька секунд.")

llm = Llama(
    model_path="phi-2.Q3_K_S.gguf",  # Шлях до моделі
    n_ctx=1024,
    n_threads=4,
    n_gpu_layers=0  # 0 — бо без GPU
)

def ask(prompt):
    """Отримати відповідь від локальної моделі"""
    output = llm(
        f"Instruct: {prompt}\nOutput:",
        max_tokens=200,
        temperature=0.7,
        top_p=0.9,
        echo=False,
    )
    text = output["choices"][0]["text"]
    return text.strip()
