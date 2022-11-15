FROM meltano/meltano:v2.9.0-python3.10

WORKDIR /home/

COPY . .

#RUN bash ./setup.sh

#RUN echo 'export NVM_DIR="$HOME/.nvm"' >> "$HOME/.zshrc"
#RUN echo '\n' >> "$HOME/.zshrc"
#RUN echo '[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"  # This loads nvm' >> "$HOME/.zshrc"
ENV PATH="$PATH:/venv/bin/meltano"
