## Model inference JSON schemas


## Create C++ Structs using quicktype

For more information vision [Quicktype GitHub repository](https://github.com/quicktype/quicktype). 

```bash
quicktype -l c++ --namespace ml --code-format with-struct --source-style single-source \
--type-style pascal-case \
--member-style camel-case \
--enumerator-style pascal-case \
--boost -s schema  \
-S schemas/input.schema.json -S schemas/trained_model.schema.json -S schemas/preprocessing.schema.json \
-o cpp/InferenceModelDefinition.hpp ./schemas/definition.schema.json
```
