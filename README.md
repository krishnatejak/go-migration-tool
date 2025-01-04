# Go Migration Tool

A tool to automate the migration of Go codebases from version 1.20 to 1.23 using Claude AI.

## Features

- Automated migration of Go files using Claude AI
- Handles go.mod and related files
- Progress tracking and resumable operations
- Rate limiting for free tier usage
- Backup system for safe migrations
- Detailed logging and progress monitoring

## Prerequisites

- Python 3.8 or higher
- Anthropic API key
- Go 1.23 installed (for testing)

## Installation

```bash
# Clone the repository
git clone https://github.com/krishnatejak/go-migration-tool.git
cd go-migration-tool

# Install dependencies
pip install -r requirements.txt
```

## Configuration

1. Set up your Anthropic API key:
```bash
export ANTHROPIC_API_KEY='your-api-key-here'
```

2. Configure the batch size and workers in `config.py` if needed

## Usage

```bash
python migrate.py --dir /path/to/your/go/project
```

Optional parameters:
```bash
--batch-size: Number of files to process in parallel (default: 2)
--max-workers: Maximum number of worker threads (default: 2)
```

## Monitoring

- Check console output for real-time progress
- View `migration.log` for detailed logs
- Monitor `migration_progress.json` for completion status

## Safety Features

- Creates backups before modifying files
- Restores from backup on failure
- Tracks progress for resumable operations
- Respects rate limits for the free tier

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT