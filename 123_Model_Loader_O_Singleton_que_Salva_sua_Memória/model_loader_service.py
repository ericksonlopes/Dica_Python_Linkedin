# pip install whisperx

import threading

import whisperx


class ModelLoaderService:
    _instance = None
    _lock = threading.Lock()
    _models = {}

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
        return cls._instance

    def get_whisper_model(self, model_size="large-v2"):
        if model_size not in self._models:
            with self._lock:
                # Double-check locking
                if model_size not in self._models:
                    print(f"🚀 Carregando modelo {model_size} pela primeira vez...")
                    # Aqui carregamos o modelo real
                    self._models[model_size] = whisperx.load_model(model_size, device="cuda")
        return self._models[model_size]

if __name__ == '__main__':
    service = ModelLoaderService()
    model1 = service.get_whisper_model("large-v2")
    model2 = service.get_whisper_model("large-v2")
    print("Modelos carregados:", model1, model2)