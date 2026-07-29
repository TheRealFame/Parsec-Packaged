# Parsec Linux Repackaging Summary

## Source
- **Original**: `https://builds.parsec.app/package/parsec-linux.deb`
- **Version**: 150-104a (build 150, revision 104a)
- **License**: Proprietary (Parsec EULA)
- **Auto-updates**: **YES** - Binary checks `builds.parsec.app` on launch and downloads new `.so` to `~/.parsec/`

---

## Created Packages

| Format | File | Size | Notes |
|--------|------|------|-------|
| **AppImage** | `parsec-x86_64.AppImage` | 1.9 MB | Portable, runs on any distro with FUSE |
| **Tarball** | `parsec-150-104a-linux-x86_64.tar.gz` | 1.7 MB | Extract and run `usr/bin/parsecd` |
| **Original .deb** | `parsec-linux.deb` | 1.5 MB | Official Parsec package |

---

## How Parsec Works (Important for Packaging)

The `.deb` is a **bootstrapper**, not the full app:
1. `/usr/bin/parsecd` (45 MB) = launcher that copies the real binary
2. `/usr/share/parsec/skel/parsecd-150-104a.so` = actual Parsec binary
3. On first run: copies `.so` to `~/.parsec/parsecd-<version>.so` and executes it
4. **Auto-updates**: On each launch, checks `builds.parsec.app`, downloads new `.so` to `~/.parsec/`

---

## Package-Specific Notes

### AppImage
- **Works**: Yes, but auto-updates write to `~/.parsec/` outside the AppImage
- **Caveat**: Updates replace the `.so` in `~/.parsec/`, not the AppImage itself
- **Recommendation**: Distribute AppImage, let Parsec handle updates internally

### Tarball
- Extract anywhere, run `./usr/bin/parsecd`
- Same auto-update behavior as AppImage

### RPM (Not Created)
- `rpmbuild` not available in build environment
- Use `alien --to-rpm parsec-linux.deb` on RPM-based distro
- Or manually create spec file (template in `rpmbuild/SPECS/parsec.spec`)

### Flatpak
- **NOT RECOMMENDED**: Sandbox blocks writing to `~/.parsec/` and executing downloaded binaries
- Would require `--filesystem=home/.parsec` + `--allow=devel` + complex workaround
- Parsec's self-updating model conflicts with Flatpak's immutable runtime

### Snap
- **NOT RECOMMENDED**: Similar confinement issues as Flatpak
- Would need `classic` confinement, defeating sandbox purpose

---

## Distribution Recommendation

| Target | Best Format |
|--------|-------------|
| **Ubuntu/Debian/Mint** | Official `.deb` (or your repackaged one) |
| **Arch/Manjaro** | Tarball or `AUR` package (build from .deb) |
| **Fedora/RHEL/openSUSE** | RPM via `alien` or manual spec |
| **Universal / Portable** | **AppImage** (this build) |
| **Steam Deck / immutable** | AppImage (copy to `~/.local/bin/`) |

---

## Files in This Directory

```
parsec-packaging/
├── parsec-x86_64.AppImage          # Ready-to-distribute AppImage
├── parsec-150-104a-linux-x86_64.tar.gz  # Generic tarball
├── parsec-linux.deb                # Original official .deb
├── appdir/                         # AppImage source (AppDir structure)
├── rpmbuild/SPECS/parsec.spec      # RPM spec template
└── PACKAGING_SUMMARY.md            # This file
```

---

## Quick Test Commands

```bash
# Test AppImage
./parsec-x86_64.AppImage --appimage-help

# Test tarball
tar -xzf parsec-150-104a-linux-x86_64.tar.gz
./usr/bin/parsecd --help

# Install .deb (Debian/Ubuntu)
sudo dpkg -i parsec-linux.deb

# Convert to RPM (on RPM distro)
sudo alien --to-rpm parsec-linux.deb
sudo rpm -i parsec-150-104a.x86_64.rpm
```
