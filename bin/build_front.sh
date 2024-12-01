echo "Installing npm dependencies."
npm ci --dev
echo "Building front."
npm run build
npm prune --production