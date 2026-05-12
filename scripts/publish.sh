#!/usr/bin/env bash
set -euo pipefail

python_packages=(
  packages/api-core
  packages/restapi
)

for package_dir in "${python_packages[@]}"; do
  (
    cd "${package_dir}"
    if [[ -n "${PYPI_TOKEN:-}" ]]; then
      poetry publish --username __token__ --password "${PYPI_TOKEN}"
    else
      poetry publish
    fi
  )
done

# npm publishing is handled by @semantic-release/npm using NPM_TOKEN.
