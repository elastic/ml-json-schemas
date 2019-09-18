## Model inference JSON schemas


## Create C++ Structs using quicktype

```bash
quicktype --namespace ml --code-format with-struct --source-style multi-source --type-style camel-case \
--member-style pascal-case --enumerator-style pascal-case --boost -s schema  \
-S schemas/input.schema.json -S schemas/evaluation.schema.json -S schemas/preprocessing.schema.json \
-o cpp/Definition.cpp ./schemas/definition.schema.json
```
