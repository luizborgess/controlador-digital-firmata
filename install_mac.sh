SWITCH="\033["
YELLOW="${SWITCH}1;33m"




if [[ $(command -v brew) == "" ]]; then
    echo "${YELLOW}Installing Homebrew"
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
else
    echo "${YELLOW}Updating Homebrew"
    brew update
fi


  
echo "${YELLOW}Instalando Python pelo Homebrew"
brew install python

echo "${YELLOW}install python requirements"

python3 -m pip install -r requirements.txt

echo "${YELLOW}Instalacao concluida"
