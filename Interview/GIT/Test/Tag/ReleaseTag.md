# 1. Anatomy of a Tag

- **Name**: e.g. `v2.1.0`, `release-2025-04-01`, `beta`.
- **Target**: a specific commit SHA.
- **Type**: lightweight vs. annotated.
- **Metadata (annotated only)**:
  - Tagger’s name & email
  - Date
  - Tag message (like a commit message)
  - (Optional) GPG signature

---

## 2. Lightweight vs. Annotated vs. Signed Tags

| Feature                    | Lightweight          | Annotated                        | Signed & Annotated               |
|----------------------------|----------------------|----------------------------------|----------------------------------|
| Stored as Git object       | No (just ref)        | Yes (full object)                | Yes (with GPG signature)         |
| Metadata (author, date…)   | No                   | Yes                              | Yes                              |
| Tag message                | No                   | Yes                              | Yes                              |
| GPG Signature Supported    | ❌                    | ❌                               | ✅                               |
| Common Use                 | Temporary bookmarks  | Official releases                | High‑security releases           |

```bash
# Annotated (default recommendation for releases)
git tag -a v2.1.0 -m "Release 2.1.0: New features & bug fixes"

# Signed (requires GPG setup)
git tag -s v2.1.0 -m "Signed release 2.1.0"
```

---

## 3. Tagging Workflows & Best Practices

1. **Semantic Versioning**  
   Follow [SemVer](https://semver.org/):  
   `MAJOR.MINOR.PATCH`  
   - Bump MAJOR for incompatible API changes  
   - Bump MINOR for new, backwards‑compatible functionality  
   - Bump PATCH for backwards‑compatible bug fixes

2. **Pre‑releases and Build Metadata**  
   - Pre‑release: `v1.0.0-alpha`, `v2.0.0-rc.1`  
   - Build metadata: `v1.0.0+exp.sha.5114f85`

3. **Automated Tagging in CI**  
   - Configure your CI (GitHub Actions, Jenkins, GitLab CI) to:
     1. Run tests, lint, build.
     2. If successful, determine next version (e.g. via `semantic-release`).
     3. Create and push annotated tag:  

        ```bash
        git tag -a $NEXT_VERSION -m "Automated release $NEXT_VERSION"
        git push origin $NEXT_VERSION
        ```

4. **Changelog Generation**  
   - Use tags as boundaries for release notes.  
   - Tools like `git-chglog`, `conventional-changelog`, or GitHub’s **Releases** page auto‑aggregate PRs/issues between tags.

---

## 4. Common Tag Commands

```bash
# List tags (simple)
git tag

# List tags with details (annotated)
git for-each-ref --format='%(refname:short) %(taggerdate)' refs/tags

# Show tag metadata
git show v2.1.0

# Describe the most recent tag reachable from HEAD
git describe --tags

# Delete a local tag
git tag -d v2.0.0

# Delete a remote tag
git push origin --delete v2.0.0

# Push all local tags to remote
git push --tags
```

---

## 5. Using Tags on GitHub

1. **Create a Release**  
   - In your repo → **Releases** → **Draft new release**.  
   - Select an existing tag or create a new one.  
   - Fill in release title, changelog, attach binaries/assets, then **Publish**.

2. **Downloadable Assets**  
   GitHub attaches built artifacts (zips, binaries) to tags—your CI can upload compiled executables to the Release.

3. **Release Automation**  
   Integrate with GitHub Actions—trigger a workflow on the `push` of a tag:

   ```yaml
   on:
     push:
       tags:
         - 'v*.*.*'
   jobs:
     build-and-publish:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         - name: Build
           run: make build
         - name: Publish Assets
           uses: softprops/action-gh-release@v1
           with:
             tag_name: ${{ github.ref_name }}
             files: build/output/*.zip
   ```

---

## 6. Advanced Techniques

- **Lightweight “Next” Tag**  
  Keep a moving `next` tag to always point at the upcoming development head:

  ```bash
  git tag -f next
  git push origin next --force
  ```

- **Tracking Changes Since Last Tag**  

  ```bash
  git log $(git describe --tags --abbrev=0)..HEAD --oneline
  ```

- **Tag Patterns for Automation**  
  Use glob patterns in CI to only trigger workflows on specific tag formats.

---

## 7. Summary of When & Why to Tag

- **Pre‑release testing**: mark internal beta points.
- **Production release**: annotate a commit you ship.
- **Hotfixes**: tag quick patches (e.g. `v2.1.1`).
- **Milestones**: major features, docs freezes.
- **Documentation**: link code examples to specific version.

---

With tags you gain a clear, immutable history of your releases, making version control, collaboration, and deployment much smoother. Feel free to ask if you want examples of integrating tags into a full CI/CD pipeline or automating changelog generation!
