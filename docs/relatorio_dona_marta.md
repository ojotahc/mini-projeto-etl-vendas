# Relatório entregue à Dona Marta

> Caso fictício. Todos os dados e nomes foram criados para estudo.

Este é o e-mail que responde à demanda do projeto: a análise das vendas da Papelaria Ponto Certo de agosto a outubro de 2026. Os valores foram conferidos contra o banco `vendas.db` e contra o painel do Power BI.

---

**Assunto:** Análise de vendas, agosto a outubro de 2026

Bom dia, Dona Marta, tudo bem?

Como solicitado, segue a análise das vendas de agosto a outubro de 2026.

**1. Quanto faturamos por mês?**

No trimestre, o faturamento foi de **R$ 6.867,30**, em 73 vendas (média de R$ 2.289,10 por mês).

| Mês | Faturamento | % do total |
|---|---|---|
| Agosto | R$ 2.589,10 | 37,7% |
| Setembro | R$ 2.366,80 | 34,5% |
| Outubro | R$ 1.911,40 | 27,8% |

Agosto foi o melhor mês. Setembro e outubro ficaram abaixo, mas, com apenas três meses de dados, é cedo para falar em tendência.

**2. Quais categorias vendem mais?**

Em faturamento, **Acessórios** lidera, com R$ 3.325,50 (cerca de 48% do total), quase o dobro de cada uma das outras. Eletrônicos (R$ 1.826,10) e Papelaria (R$ 1.715,70) ficam em patamar parecido.

Um ponto de atenção: a Papelaria tem o maior número de vendas (48 das 73), mas o menor faturamento, porque seus produtos têm preço mais baixo.

**3. Quais vendedores trazem mais resultado?**

**Fernanda** (R$ 2.086,90) e **Paulo** (R$ 2.059,60) estão praticamente empatados no topo. A diferença é de R$ 27,30 (cerca de 1,3%), pouco significativa. Marina vem em terceiro (R$ 1.466,40) e Carlos em quarto (R$ 1.056,10).

Além disso, R$ 198,30 (cerca de 3% do faturamento) correspondem a 3 vendas sem vendedor informado.

**Sobre a confiabilidade dos dados**

O arquivo exportado tinha 84 registros, e a análise usa 73:

- **4 vendas duplicadas** (lançadas duas vezes) foram removidas, o que evita inflar o faturamento.
- **7 vendas sem quantidade ou preço** foram removidas, porque sem esses dados não é possível calcular o valor da venda. Elas são cerca de 9% das vendas únicas, então o faturamento real pode ser um pouco maior que o informado.
- Vendas sem nome de vendedor ou de cliente foram mantidas e marcadas como "Não informado".
- Datas e textos foram padronizados, pois o sistema as exportava em formatos variados.

Sugiro corrigir esses lançamentos no sistema de origem, para que as próximas análises sejam mais completas.

Fico à disposição para qualquer dúvida.

Abraço,
João