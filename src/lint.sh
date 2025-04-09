isort .
ruff check .
ruff format .
git ls-files -z -- '*.html' | xargs -0r djade --target-version 5.1

npm run lint
npm run  format