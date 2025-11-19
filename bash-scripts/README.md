# Bash Scripts Collection

A collection of useful bash scripts and utilities for various tasks.

## Structure

```
bash-scripts/
├── examples/           # Example scripts
│   ├── hello.sh       # Simple hello world script
│   ├── system-info.sh # System information display
│   └── backup.sh      # File backup utility
└── utils/             # Reusable utility functions
    ├── logger.sh      # Logging utilities
    └── file-utils.sh  # File operation utilities
```

## Usage

### Making Scripts Executable

Before running any script, make it executable:

```bash
chmod +x bash-scripts/examples/hello.sh
```

### Running Example Scripts

#### Hello Script
```bash
./bash-scripts/examples/hello.sh
./bash-scripts/examples/hello.sh "Your Name"
```

#### System Info Script
```bash
./bash-scripts/examples/system-info.sh
```

#### Backup Script
```bash
./bash-scripts/examples/backup.sh /path/to/file.txt
./bash-scripts/examples/backup.sh /path/to/file.txt /path/to/backup/dir
```

### Using Utilities

Source utility files in your scripts:

```bash
#!/bin/bash
source utils/logger.sh

log_info "Starting process..."
log_success "Process completed!"
```

## Best Practices

- Always use `#!/bin/bash` as the shebang
- Use `set -e` to exit on errors
- Quote variables to handle spaces: `"$VAR"`
- Provide usage information in comments
- Make scripts executable with `chmod +x`

## Development

Add your own scripts to the `examples/` directory and shared utilities to the `utils/` directory.
