# Tradução PT-PT da base de dados

A base de dados principal continua em inglês (`characters.json`, `teamcards.json`, `crisis.json`, `gems.json`).
Esta pasta só tem **traduções**, uma por ficheiro, no formato:

```json
{
  "Texto em inglês, exatamente como está no ficheiro principal.": "Texto em português."
}
```

- Cada chave é **um parágrafo** de regras (`special_rules`, `rules`, `description`, `setup_text`, `scoring_text`).
  Os campos com vários parágrafos (`description`, `special_rules` das crises) são traduzidos parágrafo a parágrafo.
- Nomes (personagens, ataques, superpoderes, cartas, crises, tokens) **não** se traduzem.
- As palavras que a app transforma em ícones ficam em inglês e iguais: tudo o que está em MAIÚSCULAS (POWER, WOUND,
  RANGE 3, CRIT, WILD, SHORT…), as condições (Bleed, Shock…), Push/Throw/Place/Advance, Dazed, KO'd, Grunt,
  Healthy/Injured, Secure/Contest/Interact, Power Phase, Cleanup Phase.
- Se o texto em inglês de uma carta mudar, a tradução antiga deixa de corresponder e a app mostra o inglês
  até a tradução ser atualizada. Nunca aparece uma tradução desatualizada.

## Manter a tradução em dia

```bash
python3 tools/pt_missing.py
```

Mostra quantos parágrafos estão traduzidos e cria `pt/_missing.json` com o que falta (e `pt/_orphans.json` com
traduções que já não são usadas). Basta traduzir o `_missing.json` (por exemplo, pedindo ao Claude) e juntar os
pares ao ficheiro certo.

A app GELLAB MCP descarrega estes ficheiros com o resto da base de dados (lista `translations` no `manifest.json`).
