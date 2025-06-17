# Organizador Automático de Arquivos

Este projeto monitora uma pasta e organiza arquivos automaticamente por extensão, data ou nome, movendo-os para subpastas configuráveis. Ideal para automação do dia a dia, estudos de Python e portfólio.

## Como funciona

- Monitora a pasta `input/`
- Move arquivos para subpastas em `organized/` conforme extensão, data ou nome
- Gera logs automáticos das movimentações

## Exemplo de Configuração (`config.yaml`)

```yaml
watch_folder: input
organize_by: extension
destination_folder: organized
extensions_map:
  images: [".jpg", ".jpeg", ".png", ".gif"]
  documents: [".pdf", ".docx", ".txt", ".xlsx"]
  videos: [".mp4", ".avi", ".mov"]
  others: []
