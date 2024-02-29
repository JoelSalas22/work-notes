# Intro to jq

## Outline
```bash
echo '{"Key1": {"key2":"value1"}}' | jq '.'

curl https://api.github.com/repos/jqlang/jq

curl https://api.github.com/repos/jqlang/jq | jq ' .name'

curl https://api.github.com/repos/jqlang/jq | jq ' .owner'

curl https://api.github.com/repos/jqlang/jq | jq ' .owner.login'
```
## Lesson: Object Identifier-Index

```bash
jq '.key.subkey.subsubkey'
```

## Arrays

```bash
curl https://api.github.com/repos/jalang/jq/issues?per_page=5

curl https://api.github.com/repos/jalang/jq/issues?per_page=5 | jq '.[4]'

echo "[1, 2, 3, 4, 5]" | jq '.[2:4]'

echo "[1, 2, 3, 4, 5]" | jq '.[2:]'

echo "[1, 2, 3, 4, 5]" | jq '.[-2:]'
```

