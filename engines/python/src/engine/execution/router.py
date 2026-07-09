import os
import json
import time

class ExecutionRouter:
    """
    The physical execution layer for Continuum.
    This router interfaces with external LLM APIs to perform the actions defined in the YAML protocols.
    """
    def __init__(self, provider="mock"):
        self.provider = os.getenv("CONTINUUM_PROVIDER", provider)
        self.api_key = os.getenv("OPENAI_API_KEY", "")
        
    def _execute_mock(self, role: str, action: str, system_prompt: str, user_input: str) -> dict:
        """Fallback simulation mode if no API key is provided."""
        time.sleep(1.5)
        return {
            "status": "APPROVED" if action != "REVIEW_AND_CRITIQUE" else "REJECTED",
            "output": f"[MOCK GENERATION] Output from {role} performing {action}.",
            "reasoning": f"Simulated execution because CONTINUUM_PROVIDER is set to {self.provider}."
        }
        
    def _execute_openai(self, role: str, action: str, system_prompt: str, user_input: str) -> dict:
        """Real execution using OpenAI SDK (Requires openai library installed)."""
        try:
            from openai import OpenAI
            client = OpenAI(api_key=self.api_key)
            
            # We enforce JSON output so the OS can reliably parse gates.
            response = client.chat.completions.create(
                model="gpt-4o",
                response_format={"type": "json_object"},
                messages=[
                    {"role": "system", "content": f"You are the {role}. Your objective is: {action}. {system_prompt}. You MUST return JSON with keys: 'status' (APPROVED or REJECTED), 'output' (your content), and 'reasoning' (your thoughts)."},
                    {"role": "user", "content": user_input}
                ]
            )
            return json.loads(response.choices[0].message.content)
        except Exception as e:
            return {"status": "ERROR", "output": str(e), "reasoning": "Failed to connect to LLM Provider."}

    def run(self, role: str, action: str, system_prompt: str, user_input: str) -> dict:
        """Routes the execution to the correct provider based on configuration."""
        if self.provider == "openai" and self.api_key:
            return self._execute_openai(role, action, system_prompt, user_input)
        else:
            return self._execute_mock(role, action, system_prompt, user_input)
