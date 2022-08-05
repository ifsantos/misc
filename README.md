
# misc

General use repository for code snippets and its descritpions grouped by purpose

## Little about semantic commit

```
type(scope): subject
  ^    ^        ^
  |    |        |
  |    |        +-> Summary: uses the imperative, present tense: “change” not “changed” nor “changes”
  |    +----------> Scope of the change 
  +---------------> Type: chore, docs, feat, fix, refactor, style, or test.

chore: add Oyster build script
docs: explain hat wobble
feat: add beta sequence
fix: remove broken confirmation message
refactor: share logic between 4d3d3d3 and flarhgunnstow
style: convert tabs to spaces
test: ensure Tayne retains clothing
```
Example \<scope\> values: 
```
init
runner
watcher
config
web-server
proxy
etc.
```
- Breaking changes

All breaking changes have to be mentioned with a "!" at the end of type.

```
feat(runner)!: Something that breaks retrocompatibility
```


## By the way, some in-hand commands
- Reset local keys with blank password:
    ```bash
    ssh-keygen -q -N "" -t ed25519
    ```

- Check how many CPUs are there in Linux system:
    ```bash
    lscpu 
    cat /proc/cpuinfo
    top 
    htop 
    nproc 
    dmidecode -t processor 
    getconf _NPROCESSORS_ONLN 
    ```

### References
[Markdown Basic Syntax](https://www.markdownguide.org/basic-syntax/)

<http://karma-runner.github.io/6.4/dev/git-commit-msg.html>
<https://sparkbox.com/foundry/semantic_commit_messages>

