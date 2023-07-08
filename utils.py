BOLD = '\033[1m'
UNDERLINE = '\033[4m'

ENDC = '\033[0m' # End of color
OKBLUE = '\033[94m'
OKGREEN = '\033[92m' # Success
FAIL = '\033[91m' # Error
WARNING = f'{ENDC}\033[93m' # Warning
PURPLE = '\033[95m'
WHITE = '\033[37m'
GRAY = '\033[90m'
YELLOW = '\033[33m'
RED = '\033[31m'
GREEN = '\033[32m'
BLUE = '\033[34m'
CYAN = '\033[36m'


CHECKMARK = f"{ENDC}{OKGREEN}✔ "
CROSSMARK = f"{ENDC}{FAIL}✘ "
STAR = F"{BOLD}{YELLOW}★ {ENDC}"
CHAIN = f"{BOLD}{WHITE}=-=-=-=-=-=-=-=-=-=-=-=-=-={ENDC}"
OK = f"{ENDC}{OKGREEN}[{WHITE}OK{OKGREEN}]"

options = f"""{BOLD}{BLUE}[{WHITE} 1 {BLUE}]{WHITE} - {PURPLE}Create table{ENDC}
{BOLD}{BLUE}[{WHITE} 2 {BLUE}]{WHITE} - {PURPLE}Insert data{ENDC}
{BOLD}{BLUE}[{WHITE} 3 {BLUE}]{WHITE} - {PURPLE}Delete table{ENDC}
{BOLD}{FundamentusBLUE}[{WHITE} 4 {BLUE}]{WHITE} - {PURPLE}Show tables{ENDC}
{BOLD}{BLUE}[{WHITE} 0 {BLUE}]{WHITE} - {PURPLE}Exit{ENDC}"""

MENU = f"""
{BOLD}{CHAIN}
{options}
{BOLD}{CHAIN}
"""

import pandas as pd
import shutil
import os


def clear_terminal():
    # Clear the terminal
    os.system('cls' if os.name == 'nt' else 'clear')

def exit_program():
    shutil.rmtree('__pycache__')
    print(f"\n{ENDC}{GRAY}Quit program.{ENDC}")
    exit(0)


class Cleaner:
    def __init__(self, df):
        self.df = df

    def fundamentus(self):
        self.df = self.df.rename(columns={'papel': 'ativo'})
        self.df = self.df.rename(columns={'cotação': 'cotacao'})
        self.df = self.df.rename(columns={'p_ativ_circ_liq': 'p_ativo_circ'})
        self.df = self.df.rename(columns={'mrg__líq_': 'mrg_liq'})
        self.df = self.df.rename(columns={'liq__corr_': 'liq_corr'})
        self.df = self.df.rename(columns={'patrim__líq': 'patrim_liq'})
        self.df = self.df.rename(columns={'dív_brut__patrim_': 'div_bruta_patrim'})
        self.df = self.df.rename(columns={'cresc__rec_5a': 'cresc_rec_5anos'})
        return self.df
    
    def status_invest(self):
        self.df = self.df.rename(columns={'ticker': 'ativo'})
        self.df = self.df.rename(columns={'preco': 'cotacao'})
        self.df = self.df.rename(columns={'dy': 'div_yield'})
        self.df = self.df.rename(columns={'p_ativos': 'p_ativo'})
        self.df = self.df.rename(columns={'p_at_cir_liq': 'p_ativo_circ'})
        self.df = self.df.rename(columns={'margem_ebit': 'mrg_ebit'})
        self.df = self.df.rename(columns={'marg_liquida': 'mrg_liq'})
        self.df = self.df.rename(columns={'liq_corrente': 'liq_corr'})
        self.df = self.df.rename(columns={'liquidez_media_diaria': 'liq_2meses'})
        self.df = self.df.rename(columns={'div_liq___patri': 'div_bruta_patrim'})
        self.df = self.df.rename(columns={'cagr_receitas_5_anos': 'cresc_rec_5anos'})
        self.df['ev_ebitda'] = "0.00"
        self.df['patrim_liq'] = "0.00"
        return self.df
        
    def invest_site(self):
        self.df = self.df.rename(columns={'ação': 'ativo'})
        self.df = self.df.rename(columns={'p': 'cotacao'})
        self.df = self.df.rename(columns={'p_lucro': 'p_l'})
        self.df = self.df.rename(columns={'p_vpa': 'p_vp'})
        self.df = self.df.rename(columns={'p_rec_líq_': 'psr'})
        self.df = self.df.rename(columns={'p_ativo_total': 'p_ativo'})
        self.df = self.df.rename(columns={'margem_ebit': 'mrg_ebit'})
        self.df = self.df.rename(columns={'margem_líquida': 'mrg_liq'})
        self.df = self.df.rename(columns={'roinvc': 'roic'})
        self.df = self.df.rename(columns={'rpl': 'roe'})
        self.df['p_ativo_circ'] = "0.00"
        self.df['liq_corr'] = "0.00"
        self.df['liq_2meses'] = "0.00"
        self.df['patrim_liq'] = "0.00"
        self.df['div_bruta_patrim'] = "0.00"
        self.df['cresc_rec_5anos'] = "0.00"
        return self.df

    def div(self):
        self.df['div_yield'] = pd.to_numeric(self.df['div_yield'], errors='coerce') / 100
        self.df['mrg_ebit'] = pd.to_numeric(self.df['mrg_ebit'], errors='coerce') / 100
        self.df['mrg_liq'] = pd.to_numeric(self.df['mrg_liq'], errors='coerce') / 100
        self.df['roic'] = pd.to_numeric(self.df['roic'], errors='coerce') / 100
        self.df['roe'] = pd.to_numeric(self.df['roe'], errors='coerce') / 100
        self.df['cresc_rec_5anos'] = pd.to_numeric(self.df['cresc_rec_5anos'], errors='coerce') / 100
        return self.df
    