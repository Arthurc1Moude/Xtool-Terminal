document.addEventListener('DOMContentLoaded', function() {
    const outputElement = document.getElementById('output');
    const inputElement = document.getElementById('command-input');
    const commandHistory = [];
    let historyIndex = -1;
    
    // Focus the input element when the page loads
    inputElement.focus();
    
    // Keep focus on the input element when clicking anywhere in the terminal
    document.querySelector('.terminal-body').addEventListener('click', function() {
        inputElement.focus();
    });
    
    // Handle command input
    inputElement.addEventListener('keydown', function(event) {
        // If Enter key is pressed
        if (event.key === 'Enter') {
            event.preventDefault();
            
            const command = inputElement.value.trim();
            if (command) {
                // Add command to history
                commandHistory.push(command);
                historyIndex = commandHistory.length;
                
                // Display the command
                appendCommandEntry(command);
                
                // Clear the input
                inputElement.value = '';
                
                // Execute the command
                executeCommand(command);
            }
        }
        // Up arrow for command history
        else if (event.key === 'ArrowUp') {
            event.preventDefault();
            if (historyIndex > 0) {
                historyIndex--;
                inputElement.value = commandHistory[historyIndex];
                // Move cursor to end of input
                setTimeout(() => {
                    inputElement.selectionStart = inputElement.selectionEnd = inputElement.value.length;
                }, 0);
            }
        }
        // Down arrow for command history
        else if (event.key === 'ArrowDown') {
            event.preventDefault();
            if (historyIndex < commandHistory.length - 1) {
                historyIndex++;
                inputElement.value = commandHistory[historyIndex];
            } else {
                historyIndex = commandHistory.length;
                inputElement.value = '';
            }
        }
        // Tab completion
        else if (event.key === 'Tab') {
            event.preventDefault();
            // Get all command elements
            const commandElements = document.querySelectorAll('.palette-command');
            const currentInput = inputElement.value.trim();
            
            // Filter commands that start with the current input
            const matchingCommands = Array.from(commandElements)
                .map(el => el.textContent)
                .filter(cmd => cmd.startsWith(currentInput));
            
            // If there's exactly one match, complete it
            if (matchingCommands.length === 1) {
                inputElement.value = matchingCommands[0];
            }
            // If there are multiple matches, show them
            else if (matchingCommands.length > 1) {
                appendOutput('Possible commands: ' + matchingCommands.join(', '));
            }
        }
    });
    
    // Click on palette command to insert it
    document.querySelectorAll('.palette-command').forEach(cmd => {
        cmd.addEventListener('click', function() {
            inputElement.value = this.textContent;
            inputElement.focus();
        });
    });
    
    // Function to append a command entry to the output
    function appendCommandEntry(command) {
        const entryDiv = document.createElement('div');
        entryDiv.className = 'command-entry';
        
        const commandDiv = document.createElement('div');
        commandDiv.className = 'command-text';
        commandDiv.innerHTML = '<span class="prompt">user@xtool:~$</span> ' + escapeHtml(command);
        
        entryDiv.appendChild(commandDiv);
        outputElement.appendChild(entryDiv);
        
        // Scroll to bottom
        outputElement.scrollTop = outputElement.scrollHeight;
        
        return entryDiv;
    }
    
    // Function to append output to a command entry
    function appendOutput(output, isError = false) {
        const outputDiv = document.createElement('div');
        outputDiv.className = isError ? 'error-output' : 'command-output';
        outputDiv.textContent = output;
        
        outputElement.appendChild(outputDiv);
        
        // Scroll to bottom
        outputElement.scrollTop = outputElement.scrollHeight;
    }
    
    // Function to execute a command
    function executeCommand(command) {
        fetch('/execute', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ command: command }),
        })
        .then(response => response.json())
        .then(data => {
            appendOutput(data.output, data.output.startsWith('Error') || data.output.startsWith('Command not found'));
        })
        .catch(error => {
            appendOutput('Error: ' + error.message, true);
        });
    }
    
    // Helper function to escape HTML
    function escapeHtml(unsafe) {
        return unsafe
            .replace(/&/g, "&amp;")
            .replace(/</g, "&lt;")
            .replace(/>/g, "&gt;")
            .replace(/"/g, "&quot;")
            .replace(/'/g, "&#039;");
    }
    
    // Terminal control buttons functionality
    document.querySelector('.control.close').addEventListener('click', function() {
        appendOutput('Terminal session cannot be closed in web mode.', true);
    });
    
    document.querySelector('.control.minimize').addEventListener('click', function() {
        document.querySelector('.terminal-body').style.display = 
            document.querySelector('.terminal-body').style.display === 'none' ? 'flex' : 'none';
    });
    
    document.querySelector('.control.maximize').addEventListener('click', function() {
        document.querySelector('.terminal-container').classList.toggle('maximized');
    });
    
    // Add Matrix rain effect to the background
    createMatrixRain();
    
    // Function to create Matrix rain effect
    function createMatrixRain() {
        const canvas = document.createElement('canvas');
        canvas.className = 'matrix-bg';
        document.body.appendChild(canvas);
        
        const ctx = canvas.getContext('2d');
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        
        const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
        const fontSize = 14;
        const columns = canvas.width / fontSize;
        
        const drops = [];
        for (let i = 0; i < columns; i++) {
            drops[i] = 1;
        }
        
        function draw() {
            ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            
            ctx.fillStyle = '#0F0';
            ctx.font = fontSize + 'px monospace';
            
            for (let i = 0; i < drops.length; i++) {
                const text = characters.charAt(Math.floor(Math.random() * characters.length));
                ctx.fillText(text, i * fontSize, drops[i] * fontSize);
                
                if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) {
                    drops[i] = 0;
                }
                
                drops[i]++;
            }
        }
        
        setInterval(draw, 33);
    }
    
    // Handle window resize
    window.addEventListener('resize', function() {
        const canvas = document.querySelector('.matrix-bg');
        if (canvas) {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        }
    });
});