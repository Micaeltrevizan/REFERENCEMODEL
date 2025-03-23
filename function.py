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
  if 1 <= nivel <= 5:
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
  if 1 <= nivel <= 5:
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
  if 1 <= nivel <= 5:
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
  if 1 <= nivel <= 5:
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
  if 1 <= nivel <= 5:
    return tabela_tamanho[nivel], tabela_tamanho_metodologias[nivel]
  else:
    return None

