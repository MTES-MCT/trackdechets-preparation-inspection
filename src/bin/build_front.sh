echo "Installing npm dependencies."
npm ci --dev
echo "Building fronts."
npm run build
npm prune --production