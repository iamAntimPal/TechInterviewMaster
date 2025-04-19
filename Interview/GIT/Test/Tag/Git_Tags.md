## Lesson 1: What Are Git Tags & Why Use Them?

**Objective:** Understand the purpose of tags in Git.

- **Definition**: A **tag** is a reference (label) to a specific commit.
- **Use‑cases**:
  - Marking **release points** (e.g. v1.0.0)
  - Highlighting **milestones** (e.g. `alpha`, `beta`)
  - Keeping track of **stable snapshots** for deployments

> **Exercise:** In any Git repo, run `git tag`—what tags do you see? If none, imagine what commits you’d tag as “v1.0.0” or “v2.0.0-beta.”

---

## Lesson 2: Lightweight vs. Annotated vs. Signed Tags

**Objective:** Learn the three tag types and when to use each.

| Feature                   | Lightweight       | Annotated                | Signed & Annotated       |
|---------------------------|-------------------|--------------------------|--------------------------|
| Stored as Git object      | No                | Yes                      | Yes                      |
| Metadata (author, date)   | No                | Yes                      | Yes                      |
| Tag message               | No                | Yes                      | Yes                      |
| GPG Signature             | ❌                 | ❌                       | ✅                       |
| Common Use                | Temp bookmarks    | Official releases        | High‑security releases   |

```bash
# Annotated—recommended for releases
git tag -a v1.0.0 -m "Initial stable release"

# Signed—requires GPG setup
git tag -s v1.0.0 -m "Signed v1.0.0 release"
```

> **Exercise:** Create both a lightweight and an annotated tag in a trial repo. Inspect them with `git show <tag>`.

---

## Lesson 3: Creating & Listing Tags

**Objective:** Master basic tag commands.

- **Create an annotated tag**:

  ```bash
  git tag -a v2.0.0 -m "Major features added"
  ```

- **Create a lightweight tag**:

  ```bash
  git tag v2.0.1-beta
  ```

- **List all tags**:

  ```bash
  git tag
  ```

- **View details**:

  ```bash
  git show v2.0.0
  ```

> **Exercise:** Tag your current HEAD as `vTEST` and then run `git show vTEST` to inspect metadata.

---

## Lesson 4: Pushing & Sharing Tags

**Objective:** Learn how to share tags with others (your remote).

- **Push a single tag**:

  ```bash
  git push origin v1.0.0
  ```

- **Push all tags**:

  ```bash
  git push --tags
  ```

> **Tip:** Tagging locally doesn’t affect your remote until you push. Always push tags for collaborative releases.

> **Exercise:** After tagging locally, clone your repo into a new folder and verify that tags show up there only after pushing.

---

## Lesson 5: Checking Out & Using Tags

**Objective:** Understand “detached HEAD” and how to work from tags.

- **Checkout a tag**:

  ```bash
  git checkout v1.0.0
  ```

  You’re now in a **detached HEAD**—you can view code, but commits won’t belong to a branch.
- **Create a branch from a tag**:

  ```bash
  git checkout -b hotfix-from-v1.0.0
  ```

> **Exercise:** Checkout your `vTEST` tag, then create a branch `bugfix` from it and commit a small change.

---

## Lesson 6: Deleting & Renaming Tags

**Objective:** Keep your tag namespace tidy.

- **Delete a local tag**:

  ```bash
  git tag -d v1.0.1-beta
  ```

- **Delete a remote tag**:

  ```bash
  git push origin --delete v1.0.1-beta
  ```

- **Rename (re‑tag)**:

  ```bash
  git tag new-tag old-tag   # copy it
  git tag -d old-tag        # delete old
  git push origin new-tag   # push new
  git push origin --delete old-tag
  ```

> **Exercise:** Tag something, then delete it both locally and remotely. Confirm with `git tag` and `git ls-remote --tags origin`.

---

## Lesson 7: GitHub Releases & Tags

**Objective:** Leverage GitHub’s UI to turn tags into releases.

1. **On GitHub**, go to **Releases > Draft a new release**.
2. **Choose an existing tag** or **create a new one**.
3. Fill in:
   - **Release title** (e.g., “v1.0.0 — Initial stable release”)
   - **Description** / Changelog
   - **Attach binaries** (built artifacts)
4. **Publish**.

> **Exercise:** Draft a release for one of your tags. Notice GitHub automatically links to the tag’s commit.

---

## Lesson 8: Automating Tags in CI/CD

**Objective:** Integrate automatic tagging into your build pipeline.

- **Semantic‑release** or similar tools can:
  - Analyze commit messages
  - Decide next version (major/minor/patch)
  - Create & push annotated tags
  - Generate changelogs

- **GitHub Actions example**:

  ```yaml
  on:
    push:
      branches: [ main ]
  jobs:
    release:
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v3
        - uses: cycjimmy/semantic-release-action@v2
  ```

> **Exercise:** Explore a sample `.github/workflows/release.yml` that triggers on new tags to build & publish assets.

---

## Lesson 9: Best Practices & Tips

1. **Follow SemVer**: `MAJOR.MINOR.PATCH`
2. **Use annotated tags** for any public release.
3. **Sign tags** if security is critical.
4. **Automate** tagging in CI, avoid manual errors.
5. **Keep tags immutable**—if you must change, delete old and push new.
6. **Document** each release in your changelog tied to tags.

---

🔚 **Next Steps:**  

- Practice tagging in a sandbox repo.  
- Link tags to GitHub Releases and attach sample binaries.  
- Set up a simple GitHub Action that runs on tag pushes.

Feel free to ask questions or request live examples of any lesson!
