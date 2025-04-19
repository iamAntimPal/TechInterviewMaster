## 🔖 What is a Tag in Git/GitHub?

A **tag** is like a **label** or **bookmark** attached to a specific commit. It's most commonly used to:

- Mark **release versions** (e.g., `v1.0`, `v2.0-beta`)
- Highlight **milestones**
- Reference a **stable point in your project**

---

## 🛠️ Types of Tags

1. **Lightweight Tag**:  
   - Acts like a simple bookmark to a commit.
   - No extra metadata.
   - Not recommended for releases.

2. **Annotated Tag**:  
   - Contains metadata like the tagger name, email, date, and a message.
   - Stored as a full Git object.
   - Recommended for production releases.

---

## 🎯 Why Use Tags?

- To **version** your software (e.g., `v1.0.0`)
- To create **releases** on GitHub (with changelogs, zip/tar files)
- To easily **checkout** stable code
- For **deployment pipelines** or package managers

---

## 🚀 How to Use Tags in Git

### ✅ Create a Tag

**Annotated Tag:**

```bash
git tag -a v1.0 -m "Initial release version 1.0"
```

**Lightweight Tag:**

```bash
git tag v1.0
```

### 📤 Push Tag to GitHub

```bash
git push origin v1.0
```

### 🚀 Push All Tags

```bash
git push --tags
```

### 📄 List All Tags

```bash
git tag
```

### 🔄 Checkout a Tag

```bash
git checkout v1.0
```

> ⚠️ Note: When you checkout a tag, you are in a “detached HEAD” state. You can browse the code, but you can't make commits unless you create a branch.

```bash
git checkout -b new-branch-from-tag
```

---

## 🏷️ Create a Release on GitHub Using a Tag

1. Go to your repo → **Releases** tab.
2. Click **“Draft a new release.”**
3. Select an existing tag or create a new one.
4. Add title, description (changelog), and publish.

---

## 📦 Example: Semantic Versioning Tags

- `v1.0.0`: Major release
- `v1.1.0`: Minor update
- `v1.1.1`: Patch/fix

---

