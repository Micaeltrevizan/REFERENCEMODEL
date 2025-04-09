def obter_metodologia_por_fase(criticidade_nivel, equipe_nivel, dinamismo_nivel, cultura_nivel, tamanho_nivel):
    """
    Determina as metodologias recomendadas para cada fase do projeto
    baseado nos níveis dos fatores de escolha.
    """
    metodologias_por_fase = {
        "iniciação": [],
        "planejamento": [],
        "execução": [],
        "monitoramento": [],
        "encerramento": [],
    }

    # Obter as metodologias recomendadas por fator
    _, criticidade_metodologia = obter_valor_criticidade(criticidade_nivel)
    _, equipe_metodologia = obter_valor_equipe(equipe_nivel)
    _, dinamismo_metodologia = obter_valor_dinamismo(dinamismo_nivel)
    _, cultura_metodologia = obter_valor_cultura(cultura_nivel)
    _, tamanho_metodologia = obter_valor_tamanho(tamanho_nivel)

    # Mapear as metodologias para as fases correspondentes (baseado na sua tabela)
    metodologia_fase_map = {
        "Waterfall": ["iniciação", "planejamento", "execução", "encerramento"],
        "PRINCE2": ["iniciação", "planejamento", "encerramento"],
        "PMBOK": ["iniciação", "planejamento", "monitoramento", "encerramento"],
        "Scrum": ["execução", "monitoramento"],
        "XP": ["execução", "monitoramento"],
        "Kanban": ["execução"],
    }

    recomendacoes = [
        criticidade_metodologia,
        equipe_metodologia,
        dinamismo_metodologia,
        cultura_metodologia,
        tamanho_metodologia,
    ]

    for metodologia in recomendacoes:
        if metodologia in metodologia_fase_map:
            for fase in metodologia_fase_map[metodologia]:
                if metodologia not in metodologias_por_fase[fase]:
                    metodologias_por_fase[fase].append(metodologia)

    return metodologias_por_fase

def obter_valor_criticidade(nivel):
  # Tabela de correspondência: nível -> valor
  tabela_criticidade = {
    1: "Criticidade baixa",
    2: "Criticidade média",
    3: "Criticidade alta"
  }

  tabela_criticidade_metodologias = {
    1: "Kanban",
    2: "Scrum",
    3: "PRINCE2"
  }
  # Verifica se o nível informado é válido
  if 1 <= nivel <= 3: # Ajustado para o range das tabelas
    return tabela_criticidade[nivel],tabela_criticidade_metodologias[nivel]
  else:
    return None

def obter_valor_equipe(nivel):
  # Tabela de correspondência: nível -> valor
  tabela_equipe = {
    1: "Equipe inexperiente",
    2: "Equipe com experiência básica",
    3: "Equipe experiente"
  }
  tabela_equipe_metodologias = {
    1: "Waterfall",
    2: "Kanban",
    3: "XP"
  }
  # Verifica se o nível informado é válido
  if 1 <= nivel <= 3: # Ajustado para o range das tabelas
    return tabela_equipe[nivel], tabela_equipe_metodologias[nivel]
  else:
    return None

def obter_valor_dinamismo(nivel):
  # Tabela de correspondência: nível -> valor
  tabela_dinamismo = {
    1: "Dinamismo baixo",
    2: "Dinamismo médio",
    3: "Dinamismo Alto"
  }
  tabela_dinamismo_metodologias = {
    1: "Waterfall",
    2: "Scrum",
    3: "XP"
  }
  # Verifica se o nível informado é válido
  if 1 <= nivel <= 3: # Ajustado para o range das tabelas
    return tabela_dinamismo[nivel], tabela_dinamismo_metodologias[nivel]
  else:
    return None

def obter_valor_cultura(nivel):
  # Tabela de correspondência: nível -> valor
  tabela_cultura = {
    1: "Empresa Tradicional",
    2: "Empresa Neutra",
    3: "Empresa Inovadora"
  }
  tabela_cultura_metodologias = {
    1: "PRINCE2",
    2: "Scrum",
    3: "XP"
  }
  # Verifica se o nível informado é válido
  if 1 <= nivel <= 3: # Ajustado para o range das tabelas
    return tabela_cultura[nivel], tabela_cultura_metodologias[nivel]
  else:
    return None

def obter_valor_tamanho(nivel):
  # Tabela de correspondência: nível -> valor
  tabela_tamanho = {
    1: "Escopo Pequeno",
    2: "Escopo Médio",
    3: "Escopo Grande"
  }
  tabela_tamanho_metodologias = {
    1: "Kanban",
    2: "XP",
    3: "PMBOK"
  }
  # Verifica se o nível informado é válido
  if 1 <= nivel <= 3: # Ajustado para o range das tabelas
    return tabela_tamanho[nivel], tabela_tamanho_metodologias[nivel]
  else:
    return None
