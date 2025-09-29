# Utilizing Local LLMs

Local Language Models (LLMs) let you run AI on your own computer without sending data to the cloud. This is useful if you want privacy, offline support, or more control.

---

## Tools you can use

- **Ollama** – lightweight model runner.  
- **LM Studio** – desktop app to download and chat with models.  
- **VS Code extensions** – like Continue or Ollama extension for inline completions.  

---

## Why use local models?

- **Confidentiality**: Code never leaves your computer.  
- **Offline use**: Works without internet.  
- **Reproducibility**: Pin exact model versions for consistent results.  

---

## Step-by-step: Setting up Ollama with VS Code

1. **Install Ollama**  
    - Go to [https://ollama.com](https://ollama.com).  
    - Download and install for your OS.  


2. **Download a model**  
    - Open Terminal (Mac/Linux) or PowerShell (Windows).  
    - Run:  
      ```bash
      ollama pull llama3
      ```
    - This downloads the Llama 3 model.  

    ![ollama pull command](../../assets/images/ollama%20pull%20command.png)

3. **Run the model**  
      ```bash
      ollama run llama3
      ```

      - You should now be able to chat with the model in the terminal.  

      ![Screenshot of a conversation with llama3 in terminal](../../assets/images/Locall%20LLM%20terminal.png)


4. **Connect to VS Code**  

    - Install the **Continue** extension (by continue.dev) in VS Code.  
    - On the activity panel (left sidebar) open the continue extension
    - On the top right of the chat window, click on the gear icon
    - Click on "Agents" in the side-bar.
    - Click on the gear icon next to "Local Agent", this will open a `config.yaml` file. Fill it like this:


      ```yaml
      name: Local Agent
      version: 1.0.0
      schema: v1
      models:
        - name: llama3
          provider: ollama
          model: llama3:latest
      ```

    - This tells continue to use the local llama model running on your machine

    ![Continue running on local llama mode](../../assets/images/Continue%20Local%20LLM.png)

**Troubleshooting tips**  

- If the `ollama pull` command fails, check your internet connection.  
- If `ollama run` says “port already in use,” restart your computer.  
- If VS Code doesn’t connect, make sure Ollama is running in the background. 
- Larger Models can consume significant memory and run drastically slower. Gauge the right model based on you computer specifications.

---

## Best practices

- Start with smaller models (7B or 13B parameters). They run faster and use less memory.  
- Use local models for **tests, docstrings, repetitive boilerplate**.  
- Compare results against your project needs—output quality varies.  

---

## Limitations

- Larger models need powerful GPUs or lots of RAM.  
- VS Code integrations may be less polished compared to cloud tools.  

---
