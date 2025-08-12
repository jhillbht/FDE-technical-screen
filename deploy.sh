#!/bin/bash
echo '🚀 FDE Technical Screen - Replit CLI Deployment'
echo '=============================================='

# Check current directory
echo '📁 Current directory:'
pwd

# Check if we have the required files
echo ''
echo '📋 Checking project files:'
if [ -f main.py ]; then
    echo '✅ main.py found'
    echo '   Lines: '$(wc -l < main.py)
else
    echo '❌ main.py not found'
fi

if [ -f README.md ]; then
    echo '✅ README.md found'
else
    echo '❌ README.md not found'
fi

# Check Replit CLI
echo ''
echo '🔧 Checking Replit CLI:'
replit --version 2>/dev/null && echo '✅ CLI available' || echo '❌ CLI not available'

# Attempt deployment
echo ''
echo '📤 Attempting deployment:'
echo 'Command: replit push --name="FDE-Technical-Screen" --description="Package Sorting Solution for Thoughtful Automation"'

# Execute deployment
replit push --name='FDE-Technical-Screen' --description='Package Sorting Solution for Thoughtful Automation'

echo ''
echo '✅ Deployment command completed'
echo 'Check above output for success/error messages'
