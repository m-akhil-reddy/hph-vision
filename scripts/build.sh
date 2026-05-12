#!/usr/bin/env bash
set -euo pipefail

python_packages=(
  packages/api-core
  packages/restapi
)

for package_dir in "${python_packages[@]}"; do
  rm -rf "${package_dir}/dist"
  (
    cd "${package_dir}"
    poetry build
  )
done

rm -rf packages/mobile-lib/dist
mkdir -p packages/mobile-lib/dist

# The semantic-release npm plugin is responsible for creating and publishing the
# @hiperhealth/hphvision-lib npm package. CI still typechecks it before release.
yarn workspace @hiperhealth/hphvision-lib typecheck
