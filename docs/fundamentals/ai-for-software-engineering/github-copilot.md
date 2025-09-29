# Sign up & Working with GitHub Copilot

GitHub Copilot is an AI-powered coding assistant that works inside editors like Visual Studio Code (VS Code). It helps by writing code suggestions, generating boilerplate, and even drafting tests. If you’re brand new to coding tools, this guide will walk you through each step.

---

## Getting started with Copilot in VS Code

1. **Download and Install VS Code**  
      - Go to [https://code.visualstudio.com/](https://code.visualstudio.com/) and download the version for your operating system (Windows, macOS, or Linux).  
      - Install it using the installer.  

2. **Open the Extensions view**  
      - In VS Code, look at the left-hand sidebar. Click on the square-shaped icon (Extensions).  
      - In the search bar at the top of the Extensions panel, type `GitHub Copilot`.  
      - Click **Install**.  

      ![VS Code extension marketplace with Copilot highlighted](../../assets/images/Github%20copilot%20extension%20download.png)

3. **Sign in with GitHub**  
      - After installation, a pop-up will ask you to sign in.  
      - Click the sign-in button → a browser window will open → log in with your GitHub account.  
      - Free if you’re a student or part of GitHub’s verified programs; otherwise, you may need a subscription.  
   
      ![GitHub login popup in VS Code](../../assets/images/login%20to%20GH%20from%20VS%20code.png)


4. **Verify that Copilot works**  
      - Open any file (for example, a `.py` or `.js` file).  
      - Start typing a simple function like `def hello():`.  
      - If Copilot is working, you’ll see a suggestion appear faintly in your editor.  

---

## Configuring Copilot (settings.json)

Sometimes Copilot can feel “too noisy” with automatic completions. You can control this.

1. In VS Code, **open the Command Palette** (Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac)).  

2. Type `Preferences: Open User Settings (JSON)` and press Enter.  

3. In the JSON file that opens, append this snippet:  

   ```json
   {
     "editor.inlineSuggest.enabled": false,
     "github.copilot.enable": {
       "*": true
     }
   }
   ```
  ![VS Code Command Palette with 'settings.json' option](../../assets/images/GH%20settings.png)

   - This disables automatic inline suggestions but keeps Copilot active.  
   - You can trigger Copilot manually using `Ctrl+Enter` (Windows/Linux) or `Cmd+Enter` (Mac).  

---

**Troubleshooting tips**  

   - If you don’t see `settings.json`: make sure you opened “Preferences: Open User Settings (JSON)” and not the regular Settings UI.  
   - If Copilot suggestions never appear, check:  
   - Your GitHub account has Copilot access (visit [https://github.com/features/copilot](https://github.com/features/copilot)).  
   - The file type you’re editing is supported (e.g., `.py`, `.js`, `.ts`, `.java`).  

---

## Custom Instructions for Co-pilot

Projects can guide Copilot by adding a special file:

- Create `.github/copilot-instructions.md` in your repository.  
- Example content:  

```markdown
# Copilot Instructions for This Repository

- Follow project coding style (e.g., PEP 8 for Python).  
- Always include type hints.  
- Generate unit tests when adding new functions.  
- Use the standard library whenever possible.  
```

📌 **Where this applies**: These instructions influence how Copilot behaves in **chat mode** (side panel) and sometimes in completions. Since inline completions were disabled earlier, you’ll mostly see the effect in Copilot Chat suggestions.
 
![Copilot suggestions following instructions](../../assets/images/Copilot%20custom%20instructions.png)

---

## Using Copilot Chat (side panel)

Copilot isn’t only inline—it also has a **Chat view** (usually on the right side of VS Code). This works like a chatbot but with coding context.

### How to open
- Look at the Activity Bar on the left → click the Copilot icon.  
- Or press `Ctrl+Shift+I` (Windows/Linux) or `Cmd+Shift+I` (Mac).  

### Features
- **Adding context**: Select a piece of code, right-click, and choose *Ask Copilot*. It will pull that code into the chat.  
- **Switching models**: Some subscriptions allow choosing different models (e.g., GPT-4 vs GPT-3.5). You can select this in the chat panel dropdown.  
- **Ask vs Edit**:  
  - **Ask mode** → Copilot gives you advice or explains code.  
  - **Edit mode** → Copilot proposes changes that you can apply directly to your file.  

### Agent Mode
- A newer feature that allows Copilot to act as an “agent” that can carry out multi-step tasks (like running tests, refactoring multiple files).  
- You’ll see an **“agent” panel** in newer versions of VS Code with Copilot enabled.  

![Copilot Agent mode](../../assets/images/Agent%20mode.png)
![Copilot Agent mode generating code](../../assets/images/Agent%20mode%20code.png)

---

## Everyday workflows

- **Write unit tests first**: Ask Copilot Chat to generate scaffolding.  
- **Refactor code**: Highlight code and send it to Copilot Chat for suggested edits.  
- **Generate docstrings**: Place cursor inside a function, trigger Copilot Chat, and ask for a docstring.  
- **Prototype quickly**: Use Copilot for rough drafts, then refine manually.  

---

## ⚠️ Be careful

Copilot is powerful, but it has **serious pitfalls** you must stay alert to:  

- **False confidence**: It can generate code that *looks correct* but is wrong. Always run tests and read the logic carefully.  
- **Security risks**: It may suggest unsafe code (like SQL injection-prone queries or weak crypto). Treat all output as untrusted until reviewed.  
- **Licensing issues**: Long completions may accidentally resemble copyrighted code. Double-check before committing.  
- **Bad habits**: If you blindly accept everything, you may learn less and introduce subtle bugs.  
- **Data safety**: Never paste passwords, API keys, or proprietary secrets into prompts.  

Think of Copilot as a **junior developer**: fast and helpful, but needing supervision.  

---
