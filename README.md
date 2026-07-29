# Parsec Linux Repackaging

Repackages the official Parsec build into **AppImage**, **RPM**, and **Tarball** formats with GitHub Actions CI/CD.

> This README was generated with AI assistance.

## Packages Built

| Format | Use Case |
|--------|----------|
| **AppImage** | Universal Linux (any distro with FUSE) |
| **RPM (.rpm)** | Fedora, RHEL, CentOS, openSUSE |
| **Tarball (.tar.gz)** | Manual extraction, portable use |

**Note**: For Debian/Ubuntu, use the official `.deb` from [parsec.app](https://parsec.app/downloads).

## Quick Start

### Download Latest Release
Go to [Releases](https://github.com/TheRealFame/Parsec-Packaged/releases) and grab:
- `parsec-x86_64.AppImage` — run anywhere
- `parsec-*.rpm` — Fedora/RHEL
- `parsec-*.tar.gz` — generic

### Install

```bash
# AppImage (universal)
chmod +x parsec-x86_64.AppImage
./parsec-x86_64.AppImage

# RPM (Fedora/RHEL/openSUSE)
sudo rpm -i parsec-*.rpm
# or
sudo dnf install ./parsec-*.rpm

# Tarball (manual)
tar -xzf parsec-*.tar.gz
./usr/bin/parsecd
```

## Auto-Updates

**Parsec updates itself.** The launcher (`parsecd`) checks `builds.parsec.app` on every launch and downloads the latest binary to `~/.parsec/`. All package formats support this — the package only provides the initial bootstrap.

## Build Locally

```bash
# Prerequisites: docker, appimagetool
git clone https://github.com/TheRealFame/Parsec-Packaged
cd Parsec-Packaged

# Build AppImage
./appimagetool appdir parsec-x86_64.AppImage

# Build RPM (on Fedora/RHEL or via docker)
docker run --rm -v $(pwd):/src -w /src fedora:40 \
  bash -c "dnf install -y rpm-build alien && alien --to-rpm --scripts parsec-linux.deb"
```

## GitHub Actions CI/CD

Workflow: [`.github/workflows/build.yml`](.github/workflows/build.yml)

Triggers:
- Tags (`v*` or `150-*`) → creates GitHub Release with AppImage, RPM, Tarball
- Pull requests → builds artifacts

## Structure

```
Parsec-Packaged/
├── .github/workflows/build.yml   # CI/CD
├── appdir/                       # AppImage source (AppDir)
│   ├── AppRun                    # Entry point
│   ├── parsec.desktop            # Desktop entry
│   ├── parsec.png                # Icon
│   └── usr/                      # Extracted from .deb
├── parsec-linux.deb              # Official .deb (downloaded in CI)
├── rpmbuild/SPECS/parsec.spec    # RPM spec template
├── PACKAGING_TROUBLESHOOTING.md  # Common issues & fixes
├── README.md                     # This file
└── .gitignore                    # Excludes build artifacts
```

## License

Parsec is **proprietary** (Parsec EULA). This repo only repackages their official Linux build from `https://builds.parsec.app/package/parsec-linux.deb`.