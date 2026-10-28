
## Etapa 6 (2026-10-20): Reconstrução do zero + publicação com link

O arquivo HTML das etapas anteriores se perdeu (não estava salvo no
Projeto nem publicado). O usuário pediu para recriar do zero. Reconstruí
o sistema completo a partir deste documento e das 8 planilhas do Projeto:
login/cadastro, Painel de status (KPIs clicáveis, gráficos por divisão,
tabelas paginadas com filtros), Nova inspeção (Grupo → Locação → retângulos,
checklist de extintor 13 itens + CO2, checklist de hidrante 7+9+acessórios+
mangueiras, substituição, não conformidades, histórico), "Atualizar dados"
por planilha e tema roxo (agora também com modo escuro automático).

- Totais conferidos de novo: 1191 extintores / 168 hidrantes; grupos
  422/348/241/180 (1.0/2.1/3.1/4.1) e 63/50/51 (2.2/3.2/4.2), 4 hidrantes
  sem grupo — idêntico à Etapa 4b.
- **Publicado como página com link** (claude.ai/artifact/XsYzLbr8YPrFSrCTczdhzJ).
  Uma cópia do HTML ficou salva no Projeto em
  `claude/sistema-extintores-hidrantes.html` para não se perder de novo.
- Mudança forçada pela publicação: a página publicada não permite download
  de arquivo, então "Exportar CSV" virou **"Copiar CSV"** (copia para a
  área de transferência, separador `;`, pronto para colar no Excel).
- Dados (contas, inspeções) continuam salvos no navegador de cada pessoa
  (`localStorage`), sem compartilhamento entre usuários/aparelhos.
- Status do ponto de hidrante = pior status entre as mangueiras do ponto.

## Etapa 7 (2026-10-20): Cores ALBRAS + sistema de acesso (perfis)

- Paleta trocada para as cores do logo ALBRAS: azul `#2E3192`, cinza `#A8A9AD`,
  branco (status em escala azul/cinza, com ícones ✓ ! ✕ –).
- Login por e-mail/senha removido: a identidade agora é a conta Claude de
  quem abre a página (capability `user`). Dados passaram para o banco
  compartilhado da página (capability `db`): todos veem o mesmo.
- Perfis: **Administrador** = dono ou Editor no compartilhamento (automático);
  **Inspetor** e **Visualizador** definidos na nova aba "Acessos" (só admin).
  Quem nunca recebeu perfil é Visualizador. Visualizador só vê o Painel;
  Inspetor vê Painel + Nova inspeção; só Administrador vê Acessos e
  "Atualizar dados".
- Regras do banco: `perfis` e `inventario` só Editor/dono gravam
  (conferido: um Colaborador tentando gravar em `perfis` é recusado);
  `acessos/<id>` cada um grava o próprio último acesso.
- Estrutura: `insp_ext/<Nº>` e `insp_hid/<hash TAG|Local>` (histórico, um
  doc por item, últimos 120 registros); `ajustes_ext`/`ajustes_hid` (datas e
  status alterados nas inspeções); `inventario/meta` + partes (planilha
  reimportada pelo admin).
- Limite conhecido: perfis Inspetor/Visualizador são controlados pela
  página; quem foi compartilhado como Colaborador tecnicamente consegue
  gravar inspeções. Para travar de verdade, compartilhar como
  Visualizador quem só deve consultar.
- Fora da página publicada (arquivo aberto local) roda em "Modo local".

## Etapa 8 (2026-10-20): Indicadores (BI) dentro do sistema

Nova aba "Indicadores" (todos os perfis veem), com 3 páginas e dados reais:
- **Validade**: extintores (recarga +12 meses ou teste +5 anos, o que vencer
  primeiro) e mangueiras (teste hidrostático +12 meses) em Vencido / Vence em
  até 10 dias / Liberado; gráfico por divisão, vencimentos das próximas 12
  semanas e lista dos que exigem ação. Usa as datas atualizadas nas inspeções.
- **Inspeção mensal**: por locação (extintor = campo `local`, hidrante = `area`),
  itens inspecionados no mês, última inspeção, prazo = última + 30 dias e dias
  para vencer. Locação conta como concluída quando todos os itens foram
  inspecionados no mês; senão o prazo vem da inspeção do mês anterior.
  Locação sem nenhum registro aparece como "sem registro".
- **Realizado x planejado**: curva acumulada de itens, projeção no ritmo atual,
  previsão de término e avanço por grupo. Cronograma automático (locações
  distribuídas pelos dias úteis, proporcional ao nº de itens) ou editado pelo
  admin ("Editar datas").
- Banco: `mes/<AAAA-MM>` {itens: {e_<Nº>|h_<chave>: data}} gravado a cada
  inspeção salva; `plano/<AAAA-MM>` só admin grava (regra conferida).
- Gráficos com d3 7.9.0 via cdnjs (carregado ao abrir a aba).
- Existe também um BI separado de exemplo (artifact "BI Extintores e
  Hidrantes", tipo Dashboard) com dados simulados nas páginas 2 e 3.

## Etapa 9 (2026-10-20): Cronograma de atribuições

Nova aba "Cronograma" (todos veem; só admin cria/atribui):
- **Inspeções**: cada locação do mês tem data + responsável. Editor "Atribuir
  inspeções" (admin) com data/responsável por locação, "Atribuir grupo"
  (grupo inteiro para uma pessoa) e "Distribuir datas automaticamente".
  Salvo em `plano/<AAAA-MM>` {locacoes, responsaveis} (só admin grava).
  A atribuição fica concluída sozinha quando todos os itens da locação são
  inspecionados no mês; atrasada se a data passou.
- **Tarefas livres**: `tarefas/<id>` {titulo, tipoTarefa (Recarga, Teste
  hidrostático, Troca de mangueira, Sinalização, Manutenção, Outro),
  responsavel (id), data (prazo), status (A fazer/Em andamento/Concluída),
  local, descricao}. Admin cria/edita/exclui; o inspetor responsável muda a
  situação. Tarefas abertas de meses anteriores continuam aparecendo.
- Visões: "Por pessoa" (cartão por pessoa com progresso e lista) e
  "Calendário do mês" (grade seg–dom; clique no dia mostra a lista).
  Filtros pessoa / tipo / situação; inspetor abre em "Minhas atribuições".
  Botão "Inspecionar" leva à Nova inspeção já com grupo e locação.
- O cartão de cronograma do BI virou atalho para esta aba.
- Limite: tarefas são controladas pela página (regra do banco permite
  Colaborador gravar em `tarefas`).

## Etapa 10 (2026-10-20): Importação de planilha de campo + setembro/2026 (grupo 1.0)

- Nova barra em "Nova inspeção" (só admin): **Importar planilha de campo**.
  Lê o modelo ALBRAS/PREV FIRE (uma aba por sub-área) de extintores e de
  hidrantes, localiza colunas pelo texto do cabeçalho (posição varia entre
  abas), pega a data do cabeçalho ("Data: dd / mm / aaaa"), os BC(s) de
  inspeção, o checklist (C/NC/NA/NV, CO2 e pesos) e o Plano de ação — o "Nº"
  do plano é o número do extintor (sufixo da TAG, ex.: 111/27 → 27), não a
  linha. Mostra prévia antes de gravar. Item só com NA/branco = não
  inspecionado. Reimportar não duplica (campo `importId`).
- Grava: histórico em `insp_ext/<Nº>`, mês em `mes/<AAAA-MM>`, e datas de
  recarga/teste mais novas que o inventário em `ajustes_ext`.
- Carregado no banco: "1.0 Extintores - Planilhas preenchida - Setembro 2026":
  305 inspeções (30 abas), 144 datas de recarga/teste atualizadas, 118 itens
  sem preenchimento (abas sem data: 111SA_2, 112, 113, 122, 123, 141SA/SB,
  143). 4 extintores da aba 123 (123/01–04) não existem no inventário.
- Pausado a pedido do usuário: aba "Mangueiras" no Cronograma (rascunho em
  src/mg_html.html, não integrado).

## Etapa 11 (2026-10-20): Setembro/2026 completo (todos os grupos)

- Importadas as planilhas de setembro 2.1, 2.2, 3.1, 3.2, 4.1 e 4.2 (além da
  1.0 já carregada). Ajustes no importador: cabeçalho com erro de digitação
  ("Núimero", "Nmúmero") agora é reconhecido pela célula com "Data:"/"Mês";
  Nº só com número (ex.: "4") vira "615/04" pelo prefixo da aba; hidrante
  casa também por TAG + código da área quando o texto do local difere.
- Folhas sem data no cabeçalho (não importadas): 3.1 → 613, 715.
- Não encontrados no inventário: 4.1 → 711/06, 711/07, 954/01–05, 967/01;
  3.2 → 814 TAG 1 (Portaria 3), 822 TAG 2 (Área de Inflamáveis);
  4.2 → 712 TAG 2 (depósito da Brigada), 722 TAG 1 (em frente ao TI).
  Os 4 hidrantes provavelmente são os 4 pontos sem grupo do inventário
  (Portaria III, Posto de combustível, Brigada, TI) com TAG/local escritos
  diferente — aguardando confirmação do usuário.

## Etapa 12 (2026-10-20): Cadastro de pessoas + perfis da brigada

- Aba "Acessos" virou **"Pessoas"** (Administrador e Supervisor veem; só
  Administrador altera). Cadastro em `pessoas/<id>`: nome, matrícula (única),
  função (sugestões: Supervisor, BC Líder, Bombeiro Civil…), turno (A/B/C/D/ADM),
  equipe, grupos de inspeção (1.0…4.2), perfil, conta Claude vinculada (uid,
  opcional) e ativo. Lista de "contas que entraram sem cadastro" para cadastrar.
- **5 perfis**: Administrador (tudo; precisa ser Editor da página), Supervisor
  (planeja cronograma, importa planilha de campo, inspeciona, vê cadastro),
  BC Líder (inspeciona, importa planilha, vê cronograma de todos, atualiza
  tarefas), BC Inspetor (inspeciona, vê as próprias atribuições), Visualizador
  (painel e indicadores). Perfil vem do cadastro vinculado à conta; antigos
  `perfis/<uid>` continuam valendo para quem não tem cadastro.
- Pessoas sem conta podem receber atribuições no Cronograma ("p:<id>", aparece
  como "(sem conta)").
- Regras do banco: `pessoas` só Editor/dono grava (conferido); `plano` liberado
  para Colaborador (Supervisor planeja; controle feito pela página).

## Etapa 13 (2026-10-20): Perfis de acesso personalizáveis

- Tela "Pessoas" ganhou duas abas: **Usuários** (cadastro, botão "Cadastrar
  usuário") e **Perfis de acesso** (editor). Admin cria perfis novos ("Novo
  perfil", podendo copiar permissões de outro), renomeia e marca permissões;
  perfis padrão podem ser ajustados e "Restaurar padrão"; perfis criados podem
  ser excluídos se ninguém usar. Administrador fica sempre com tudo.
- Permissões: ver indicadores, registrar inspeções, importar planilhas de
  campo, ver cronograma da equipe, atualizar tarefas da equipe, planejar
  cronograma, consultar cadastro, cadastrar pessoas/editar perfis (exige
  Editor), atualizar inventário (exige Editor). Painel de status todos veem.
- Banco: `perfis_def/<id>` {nome, perms[], ordem} — só Editor/dono grava
  (conferido). Padrões ficam no código (admin, supervisor, lider, inspetor,
  visualizador) e o banco sobrepõe.

## Etapa 14 — Login com "Sair" e "Voltar" (v10)
- Tela de login ao abrir: matrícula + PIN (4–8 dígitos), ou atalhos "Continuar como <pessoa vinculada à conta Claude>", "Entrar como administrador" (dono/editor) e "Entrar como visitante" (só consulta).
- Botão **Sair** no topo volta à tela de login; a sessão fica salva no navegador por 12 h (voltar sem digitar de novo).
- PIN definido pelo administrador no cadastro da pessoa (campo "PIN de acesso"; botão "Remover PIN"). Guardado como PBKDF2-SHA-256 com sal em `pessoas/<id>` (`pinSalt`, `pinHash`).
- Perfil ativo = perfil da pessoa que entrou (mesmo que a conta Claude seja de outro). Inspeções gravam `inspetor` (nome) e `pessoa` (id); "Minhas atribuições" seguem a pessoa logada.
- 5 PINs errados → espera de 30 s. Cadastro desativado derruba a sessão.
- Limite: o PIN é uma trava de uso compartilhado; a permissão de gravar no banco continua dependendo do compartilhamento da página (conta Claude).

## Etapa 15 — Primeiro acesso na tela de login (v11)
- Link "Primeiro acesso? Solicite seu cadastro" na tela de login: nome, matrícula, turno, função, equipe e PIN (com confirmação). Opção de vincular a conta Claude do aparelho.
- Grava em `solicitacoes/m_<matrícula>` (PIN já com PBKDF2 + sal). Matrícula já cadastrada é recusada; tentar entrar antes da aprovação mostra "aguarda aprovação".
- Admin vê contador no botão Pessoas e o bloco "Solicitações de primeiro acesso": Revisar e aprovar (abre o cadastro preenchido, perfil sugerido pela função) ou Recusar. Ao aprovar, cria `pessoas/<id>` com o PIN e apaga a solicitação.

## Etapa 16 — Vencimentos no último dia útil + inspeção mensal por item (v12)
- Vencimento = último dia útil do mês do aniversário (sem sáb/dom, feriados nacionais fixos e Sexta-feira Santa): recarga +1 ano, teste hidrostático do extintor +5 anos, teste da mangueira +1 ano. Usado no status do Painel, no BI (Validade) e no CSV.
- Status das mangueiras agora é recalculado pela data do teste (antes vinha pronto da planilha); sem data, mantém o da planilha.
- Painel (Extintores/Hidrantes): sob cada data de recarga/teste aparece "vence dd/mm/aaaa"; nova coluna "Inspeção mensal" (última + vence).
- Inspeção mensal: vale até o último dia do mês seguinte ao da última inspeção. Situação: Em dia / Fazer este mês / Vencida / Sem registro. Lê todos os meses de `mes/*` (S.ouvirMesTodos → ULT_INSP).
- BI Inspeção mensal: coluna "Vencimento" com a nova regra (substitui +30 dias).

## Etapa 17 — Datas no último dia do mês + Locação no lugar do Nº (v13)
- Realização (recarga, teste do extintor, teste da mangueira) exibida no último dia do mês em que foi feita; vencimento também no último dia do mês (calendário, substitui o "dia útil" da v12).
- Tabela de Extintores e CSV: coluna Nº removida; Locação (TAG) é a primeira coluna. Busca continua aceitando o Nº.

## Etapa 18 — BC Básico + áreas por equipe/pessoa (v14)
- Perfil padrão "inspetor" renomeado para **BC Básico** (função "BC Básico" sugere esse perfil).
- Nova permissão `verTodasAreas` (Admin e Supervisor). Quem não tem vê só os grupos atribuídos.
- Pessoas → aba **Equipes e áreas**: resumo por grupo (qtd. extintores/hidrantes), atribuição por equipe (campo Equipe do cadastro) e por pessoa; salva ao marcar. Coleção `areas`: `eq_<slug>` {nome, grupos} e `p_<pessoaId>` {grupos}. Editável por quem tem planejar ou cadastrar.
- Área visível = grupos da equipe ∪ grupos da pessoa; filtro aplicado em montar() (Painel, Nova inspeção, BI, Cronograma). Sem nada atribuído → vê tudo (aviso). Faixa "Áreas" no topo mostra o recorte.
- Campo de grupos saiu do formulário da pessoa (aponta para a aba nova). Grupos: 1.0/2.1/3.1/4.1 = extintores; 2.2/3.2/4.2 = hidrantes.

## Etapa 19 — Distribuição de planilhas por equipe + alterar dados do equipamento (v15)
- Cronograma → aba **Distribuição de planilhas** (padrão): por mês, Equipe, Líder, Recebimento, Devolução, Prazo, Status (Em andamento / Atrasada / Concluída / Concluída atrasada), Planilha (grupos), Progresso (itens inspecionados desde o recebimento), Anotações, Próxima planilha. Cartões mostram com qual equipe está cada grupo.
- Coleção `entregas/<id>` {mes, equipe, lideres, grupos[], recebimento, prazo, devolucao|null, anotacoes}. Trava: grupo com entrega aberta (sem devolução) fica bloqueado para outra equipe. Entregar/editar: planejar (Adm/Supervisor). Devolução: planejar ou BC Líder da própria equipe.
- Equipe com planilha aberta vê automaticamente esses grupos (soma com áreas fixas). Equipes padrão: Alfa, Bravo, Charlie, Delta.
- Atribuir inspeções: o filtro Grupo mostra só as locações do grupo; responsável pode ser Equipe (eq:<slug>) ou pessoa; ao escolher o grupo, sugere a equipe que está com a planilha. Sem responsável, a locação fica com a equipe da planilha. "Minhas atribuições" inclui a equipe.
- "Alterar dados" (extintor: nº fabricação, tipo, recarga, teste; hidrante: nº fabricação e teste de cada mangueira) em Nova inspeção e no ✎ das tabelas do Painel; motivo + observação; histórico em ajustes_*/historico.
- Setembro/2026 lançado no banco a partir do controle: Bravo 1.0; Charlie 4.1/4.2; Alfa 3.1/3.2; Delta 2.1/2.2 (todas concluídas atrasadas). Outubro (Bravo 2.1/2.2, Charlie 3.1/3.2, Alfa 4.1/4.2, Delta 1.0) ainda não lançado — faltam as datas.
- (v16) Progresso clicável na Distribuição de planilhas: abre a lista Faltando / Realizados da planilha (contagem realizados/total geral e por extintor/hidrante, busca, filtro por local, Copiar lista).

## Etapa 20 — Líder programa a própria equipe (v17)
- Nova permissão `programar` (padrão no BC Líder): "Atribuir inspeções" e "Nova tarefa" liberados, limitados às locações dos grupos da equipe dele (planilha aberta + áreas) e com responsáveis só da equipe (a equipe, ele mesmo e os membros). Edita tarefas que criou ou da equipe.
- Supervisor e Adm (planejar) continuam programando tudo e são os únicos que entregam planilhas.
- Salvar atribuições agora mescla com o plano existente (só altera as locações que a pessoa pode programar).

## Etapa 21 — Gerar planilhas do mês a partir do modelo em branco (v18)
- Cronograma → Distribuição de planilhas → **Gerar planilhas do mês** (Adm, Supervisor, Líder ou quem importa planilhas de campo). Envia um ou vários .xlsx em branco (modelo ALBRAS/PREV FIRE de extintores ou hidrantes); escolhe mês atual ou próximo.
- Edita o XML do próprio arquivo (JSZip 3.10.1 via cdnjs), mantendo toda a formatação: troca "Mês: X / AAAA", "Data: / MM / AAAA" e "ALBRAS/AAAA"; atualiza Tipo, Nº fabricação, Última recarga e Último teste (extintores, por locação) e Último teste das mangueiras (hidrantes, por TAG + localização/área), só quando o mês ou o valor mudou (datas gravadas como dia 01, padrão do modelo). Remove calcChain.
- Mostra o que mudou e o que não foi encontrado; botão Baixar usa a capacidade `downloads` (adicionada na v18). Nome do arquivo troca o mês (ex.: "... Julho 2026" → "... Novembro 2026").

## Etapa 22 — Planilhas preenchidas do mês anterior → mês seguinte + Retirar do controle (v19)
- "Gerar planilhas do mês" aceita planilhas preenchidas: limpa marcações C/NC/NV/X (mantém NA, pesos e quantidades), limpa o plano de ação, zera o dia da Data e troca mês/ano (aceita "Mês: JULHO", "Mês: Julho / 2026" e "Julho/2020 Data: 17/07/2020").
- Datas de recarga/teste só avançam (nunca volta para uma data mais antiga que a da planilha).
- **Retirar do controle**: no "Alterar dados" (Adm, Supervisor, Líder ou inventário) marca o extintor/hidrante como retirado (ajuste `retirado` + `retiradoMotivo`, com histórico). Sai do painel, inspeções, BI, cronograma e planilhas; aparece no filtro Status → "Retirado do controle" e pode voltar.
- Ao gerar, linhas de itens retirados saem da planilha e as de baixo sobem (só valores; formatação de cada linha fica). Aponta "Possíveis saídas do controle": "Não encontrado" = NC/X ou plano de ação com retirado/removido/baixado/desativado/transferido; botão Retirar do controle + "Gerar de novo sem os retirados".

## Etapa 23 — Responsável no rodapé da planilha gerada (v20)
- Opção "Responsável e líder no rodapé": preenche "BC(s) Inspecionador(es):" com os responsáveis atribuídos às locações da aba no mês escolhido (plano/<AAAA-MM>) ou, sem atribuição, "Equipe X" da planilha entregue para o grupo naquele mês (ou a que está com o grupo); "BC Líder:" com os líderes da entrega. Mantém "Supervisor:" e o espaçamento. Sem responsável, limpa os nomes do mês anterior.
- Correção: a limpeza do plano de ação parava só em "Leganda"; agora para em Legenda/Leganda/BC(s)/Supervisor (antes podia apagar a legenda e o rodapé das planilhas de hidrantes). Marca "SA" (Sem Acesso) também é limpa.

## Etapa 24 — Atualiza mesmo com informação faltando (v21)
- Gerar planilhas nunca trava: cada aba é processada separadamente (aba com formato diferente fica como estava e é listada). Rodapé usa a entrega do mês → a aberta → a mais recente do grupo; líder cai para os BC Líder cadastrados na equipe. Sem nenhuma, gera assim mesmo e avisa.
- Itens da planilha que não estão no sistema: botão **Incluir no sistema** grava em `novos/<id>` com o que a planilha tem (locação, localização, tipo, fabricação, recarga, teste; hidrante: TAG, localização, testes das mangueiras) + Unidade/Área do cabeçalho e o grupo da aba. Entram no painel, inspeções, BI e planilhas; o que faltar fica em branco para completar no "Alterar dados".

## Etapa 25 — Comparativo de grupos (v22)
- Indicadores → aba **Comparativo de grupos**: por mês (‹ ›), Por grupo ou Por equipe. Frase-resumo, KPIs (realizado geral, maior, menor, diferença em p.p. e média), ranking com barra de % realizado, itens realizados/total, extintores, hidrantes, faltando e status/duração da planilha da equipe; mapa de calor dos últimos 6 meses por grupo.
- Realizado = itens com inspeção registrada em `mes/<AAAA-MM>` sobre os itens ativos do grupo (sem retirados; respeita a restrição de áreas). ouvirMesTodos agora entrega também o mapa por mês (MES_TODOS).
- Setembro/2026: 86,4% geral; 4.1 e 3.2 com 100%, 1.0 com 72,3%. Por equipe: Charlie 97,8%, Alfa 93,5%, Delta 89,5%, Bravo 72,3%.

## Etapa 26 — Importar planilhas de meses anteriores (v23)
- Botão **Importar meses anteriores** (Indicadores → Comparativo de grupos) e **Meses anteriores** (barra de Nova inspeção), para quem importa planilhas de campo.
- Vários arquivos de uma vez; mês pelo cabeçalho de cada folha ou forçado (últimos 13 meses); folhas sem o dia na Data usam o último dia do mês (opção). Mostra por arquivo: mês, folhas, inspeções, NC, datas atualizadas, avisos; "Importar tudo" grava (sem duplicar: importId) e marca `mes/<AAAA-MM>`.
- Cabeçalho reconhece "Mês: JULHO", "Julho/2020 Data: 17/07/2020" e ano pela Data. Casamento usa todos os itens (incluindo retirados e incluídos).
- Comparativo: maior/menor considera só grupos com inspeção ou planilha entregue naquele mês.
- Teste com 4.1 e 4.2 de julho/2026: 40 inspeções (a 4.1 de julho tem poucas marcações).

## Etapa 27 — Ver as inspeções de meses anteriores (v24)
- No Comparativo de grupos: clicar numa linha (grupo ou equipe) ou numa célula do mapa de 6 meses abre a janela do mês: Realizados (data, inspetor, NC), Com não conformidade, Faltando (última inspeção antes do mês). Setas ‹ › navegam pelos meses; busca, filtro por local e Copiar lista.
- Lê o histórico de `insp_ext`/`insp_hid` uma vez (cache de 2 min).

## Etapa 28 — Painel → Inspeções por mês (v25)
- Aba simples no Painel de status: escolhe o Mês (lista mostra quantos itens cada mês tem), Grupo, Resultado (conformes / com NC) e busca; tabela única com Data, Item, Grupo, Local, Localização, Inspetor e Resultado (✓ Conforme / ✕ Não conforme + texto). Paginada, Copiar CSV. Abre no mês atual ou, se vazio, no último mês com inspeções.

## Etapa 29 — Correção do Progresso da planilha (v26)
- Progresso/Faltando de cada entrega passou a contar as inspeções registradas dentro do período da planilha (recebimento → devolução) mês a mês (`mes/*`), e não só a última inspeção de cada item. Antes, a importação de outubro (grupo 1.0) zerou o progresso da Bravo em setembro (0/427); agora volta a mostrar o realizado correto.

## Etapa 30 — Retirar direto da lista "Faltando" (v27)
- Nas listas Faltando (Comparativo → janela do mês e Progresso da planilha) há o botão "Retirar do controle" (2 cliques para confirmar), para itens que não estão mais na planilha.
- 27/10/2026: retirados no banco os 5 itens incluídos pela planilha de outubro do 1.0 que não constam mais nela: 123/01, 123/02, 123/03, 123/04 e 132/06 (ajustes_ext/N123_0x e N132_06, motivo "Não consta mais na planilha"). Grupo 1.0 em outubro: 422 de 422.

## Etapa 31 — Escolher o mês no Realizado x planejado (v28)
- Setas ‹ mês › e "Voltar para o mês atual" na aba Realizado x planejado. Meses passados mostram curva até o fim do mês (marcador "fim do mês", sem projeção), KPIs Realizado no mês / Planejado / Faltou / Ritmo médio, e o cronograma salvo daquele mês (plano/<AAAA-MM>, lido sob demanda) ou a distribuição automática. Edição de datas só no mês atual.
- Dados reais: agosto/2026 79% (1.070 de 1.359), setembro 86% (1.171).
- (v29) Gráfico "Por grupo de inspeção" conta cada item pelo próprio grupo (antes usava o grupo da locação e misturava itens: 1.0 aparecia 422 de 437, 2.1 com 253, 3.1 com 321). Agora 1.0 = 422 de 422, 2.1 = 348, 3.1 = 241; "Sem grupo" = 4 hidrantes sem grupo (814, 822, 712, 722).

## Etapa 32 — Realizado x planejado separado por grupo (v30)
- Botões "Todos os grupos / Grupo 1.0 … 4.2" acima dos KPIs: KPIs, frase, curva e barras passam a considerar só os itens do grupo escolhido (pelo grupo de cada item), em qualquer mês. Frase "Concluído" quando o grupo fechou 100%, "Em dia" quando o desvio é zero.
- Outubro/2026: 1.0 concluído (422/422); 2.1 0 de 348. Setembro: 2.1 fechou com 89% (311/348).

## Etapa 33 — Comparar com a equipe anterior (v31)
- Realizado x planejado → "Comparar com: Equipe anterior (mesmo grupo) | Cronograma" (padrão: equipe anterior). A linha cinza vira o avanço acumulado, dia a dia, da equipe que fez o mesmo grupo na entrega anterior (último `entregas` com o grupo e mês < atual; sem grupo escolhido, o mês anterior). KPIs: equipe atual até o dia X, equipe anterior até o dia X, diferença (à frente/atrás) e total da anterior no mês. Sem dados do mês anterior, volta ao cronograma.
- Exemplo real: grupo 1.0 — Delta 422 até 27/10 x Bravo 305 até 27/09 (+117).
- (v32) Filtro "Tudo | Extintores | Mangueiras (hidrantes)" no Realizado x planejado (combina com grupo, mês e comparação). Grupos listados conforme o tipo; nomes das equipes filtrados pelos grupos do tipo. Em mês passado a comparação é mês inteiro x mês inteiro.

## Etapa 34 — Próxima inspeção mensal = mesmo dia do mês seguinte (v33)
- Vencimento da inspeção mensal: data da última inspeção + 1 mês, mesmo dia (20/10 → 20/11); se o dia não existir no mês seguinte (30/01 → fevereiro, 31/03 → abril), cai no último dia do mês (28/02 ou 29/02 em ano bissexto; 30/04). Substitui a regra "último dia do mês seguinte".
- Situação do item: Em dia (> 7 dias), Vence em breve (≤ 7 dias), Vencida, Sem registro. Locação: vencimento = o item que vence primeiro; "(mês anterior)" só quando essa inspeção é de mês anterior.

## Etapa 35 — Baixar cópia atualizada (offline) (v34)
- Problema: a página .html baixada abre em "modo local", sem o banco compartilhado, então mostrava só o inventário original.
- Botão **Baixar cópia** no topo (Adm/Supervisor/inventário, só online): monta um .html com todos os dados do momento embutidos (ajustes, meses, planos, entregas, itens incluídos, perfis, tarefas, pessoas sem PIN, áreas, histórico de inspeções e inventário reimportado). Ao abrir sem internet/fora do Claude, mostra tudo com a faixa "Cópia offline — dados de dd/mm hh:mm", só para consulta (alterações ficam só na memória da cópia).
- Implementação: FONTE_PAGINA capturada no início do script (scripts `data-app`), `<script id="snap-data">` recebe o JSON; lsGet/lsSet usam MEM quando há snapshot; ouvirPessoas/ouvirAreas locais leem pessoas_v1/areas_v1.

## Etapa 36 — Menu lateral à esquerda (v35)
- Em telas ≥ 1000 px o menu vira barra lateral fixa à esquerda (232 px): marca no topo, itens com ícones (Painel, Nova inspeção, Cronograma, Indicadores, Pessoas — com contador de solicitações), e no rodapé Atualizar dados, nome + perfil, Baixar cópia e Sair. Conteúdo à direita (até 1280 px).
- Em celular/telas menores continua a barra no topo; em ≤ 700 px os botões Atualizar dados e Baixar cópia ficam ocultos.
- (v36) Botão "Baixar cópia" removido a pedido (a função gerarCopiaOffline continua no código, sem botão).

## Etapa 37 — Realizado por dia no gráfico (v37)
- Avanço acumulado: rótulo "+N" acima de cada dia com inspeção (quanto foi feito no dia); tooltip mostra "Feito no dia: +X extintores · +Y hidrantes", o acumulado e a referência (com o quanto a equipe anterior fez naquele dia).
- Abaixo do gráfico: "Ver o realizado por dia" — tabela Dia | Extintores | Hidrantes | Total no dia | Acumulado. Respeita mês, grupo e tipo escolhidos.

## Etapa 38 — Sinalização na Nova inspeção (v38)
- Cartões de extintor/hidrante: faixa lateral e etiqueta "✕ Vencido" (recarga/teste), "! Atenção" (até 60 dias), "✓ Mês" (já inspecionado no mês, também ✓ ao lado do número) e "⏰ Inspeção" (inspeção mensal vencida). Dica ao passar o mouse com datas.
- Filtro "Mostrar": Todos / Vencidos / Falta inspecionar no mês / Já inspecionados no mês; resumo no topo da lista (total · vencidos · feitos · faltando); legenda das etiquetas.
- (v39) Status 'Atenção' (recarga/teste e mangueiras) passou de 60 para 10 dias antes do vencimento, em todo o sistema.
- (v40) Dentro do Claude sem acesso ao banco (não logado / sem compartilhamento): mostra aviso na tela inicial em vez de abrir em modo local. Fora do Claude (arquivo baixado/pré-visualização) a faixa explica que é uma cópia sem banco e orienta abrir pelo link.

## Etapa 39 — Aparelho compartilhado da brigada (v41)
- Botão no menu (só Administrador): "Aparelho compartilhado: ligado/desligado" — vale por navegador/aparelho (localStorage `exh-aparelho-compartilhado`). Só liga se existir uma pessoa ativa com perfil Administrador, matrícula e PIN (para não trancar o admin); ao ligar, sai da sessão.
- Ligado: tela de login só com matrícula + PIN, Primeiro acesso e Visitante (some "Continuar como" e "Entrar como administrador"); aviso explicando o uso; saída automática após 15 min sem uso (também ao recarregar depois de 15 min parado).
- Uso: tablet/computador da brigada com uma conta Claude conectada e o link aberto; cada pessoa entra com matrícula/PIN e clica Sair.
- (v42) Inspeções por mês: coluna Nº fabricação (extintor; hidrante mostra o das mangueiras, se cadastrado), também na busca e no CSV.

## Etapa 40 — Publicação na Vercel com banco Firebase (v43)
- `dist/index.html` (Vercel) carrega o Firebase (app/auth/firestore compat 10.12.2) e `firebase-config.js`; `dist/sistema-extintores-hidrantes.html` continua sendo a versão do Artifact no Claude.
- Fora do Claude, com `FIREBASE_CONFIG` preenchido: login anônimo no Firebase + entrada por matrícula e PIN (sem conta Claude). Sem configuração: aviso "Banco ainda não configurado".
- Primeira configuração: se não existe administrador com PIN, a tela de login pede para criar o primeiro administrador.
- "Importar backup" (só Administrador, no Firebase): traz o arquivo .json exportado do banco do Artifact (inspeções, ajustes, meses, planos, entregas, novos, pessoas).
- Regras do Firestore em `firestore.rules` (leitura/gravação para quem abriu o site; o controle de acesso é pela matrícula/PIN).
