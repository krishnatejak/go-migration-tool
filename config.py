# Configuration settings for the migration tool

# Claude API settings
MODEL_NAME = "claude-3-sonnet-20241022"

# Rate limits for free tier
REQUESTS_PER_MINUTE = 5
INPUT_TOKENS_PER_MINUTE = 20000
OUTPUT_TOKENS_PER_MINUTE = 4000

# Batch processing settings
DEFAULT_BATCH_SIZE = 2
DEFAULT_MAX_WORKERS = 2
BATCH_DELAY_SECONDS = 2

# File patterns
IGNORE_PATTERNS = ['vendor/', 'test/']
FILE_PATTERNS = ['.go', 'go.mod', 'go.sum']

# Backup settings
BACKUP_DIR = "go_migration_backup"

# Logging settings
LOG_FILE = "migration.log"
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'

# Progress tracking
PROGRESS_FILE = "migration_progress.json"