# Parsec Packaging Troubleshooting

Common issues when building or running Parsec packages.

## AppImage Issues

### AppImage won't run (FUSE missing)
```bash
# Ubuntu/Debian
sudo apt install fuse libfuse2

# Fedora/RHEL
sudo dnf install fuse

# Arch/Manjaro
sudo pacman -S fuse2
```

### Permission denied
```bash
chmod +x parsec-x86_64.AppImage
```

### AppImage runs but Parsec doesn't launch
- Check `~/.parsec/` exists and is writable
- Run with `--appimage-extract-and-run` to debug extraction
- Check `dmesg | grep -i fuse` for kernel issues

## Debian/Ubuntu Issues

### dpkg dependency errors
```bash
sudo apt-get install -f
sudo dpkg -i parsec_*.deb
```

### Missing libssl version
Parsec depends on `libssl3 | libssl1.1 | libssl1.0.0`. On newer distros:
```bash
# Ubuntu 24.04+ has libssl3
# Older: install libssl1.1 from universe
sudo apt install libssl1.1
```

## RPM Issues (Fedora/RHEL/openSUSE)

### alien conversion fails
```bash
# Ensure you have the .deb first
wget https://builds.parsec.app/package/parsec-linux.deb
alien --to-rpm --scripts parsec-linux.deb
```

### RPM install fails with dependencies
```bash
# Install with dnf/yum to auto-resolve
sudo dnf install ./parsec-*.rpm
# or
sudo yum localinstall ./parsec-*.rpm
```

## Auto-Update Conflicts

### Parsec says "Please reinstall from parsec.app"
- The `~/.parsec/parsecd-*.so` is corrupted or version mismatch
- Fix: `rm -rf ~/.parsec/` and relaunch

### Multiple Parsec versions conflict
- AppImage + system package both create `~/.parsec/`
- They share the same auto-update directory (this is fine)
- Last launched version wins

## Build Issues (CI/CD)

### GitHub Actions: "No space left on device"
- Self-hosted runners need disk space
- Use `actions/cache` for `~/.parsec/` between runs (optional)

### appimagetool: "AppStream metadata missing"
- Warning only, not an error
- Add `usr/share/metainfo/parsec.appdata.xml` to silence

### RPM build: "alien: command not found"
```yaml
# In workflow:
- run: sudo apt-get install -y alien rpm
```

## Distribution-Specific Notes

### Ubuntu 22.04 / 24.04
- Works out of the box
- libssl3 available

### Debian 12 (Bookworm)
- Needs libssl1.1 from backports or manual install

### Fedora 39/40
- Works with `dnf install ./parsec.rpm`
- Uses libssl3

### Arch Linux
- Rolling, always latest deps
- `makepkg` builds clean package

### openSUSE Tumbleweed/Leap
- Use `alien --to-rpm` then `zypper in ./parsec.rpm`

## Reporting Issues

If you encounter a packaging issue:
1. Check this file first
2. Run with verbose output: `./parsec-x86_64.AppImage --verbose`
3. Check `~/.parsec/` logs
4. Open issue on [GitHub](https://github.com/TheRealFame/parsec-packaging/issues)

Include:
- Distro & version
- Package format used
- Error message
- `ldd usr/bin/parsecd` output (for missing libs)