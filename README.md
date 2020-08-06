# AraoSurveillance

Record your IP cameras in local.
- eMail notification on record errors
- Automatically remove older videos in case of low free disk
- Automatically split camera stream


### Installation

- Clone project:

      git clone https://github.com/estevopaz/AraoSurveillance.git

- System requirements (GNU/Linux Debian):

      apt install python3-psutil python3-setuptools
      
- System installation (as __root__):

      cd AraoSurveillance
      ./setup.py install


### Configuration

Configuration must be done as __root__:

- Create system __camera__ user and group:

      adduser camera --no-create-home --disabled-login

- Copy configuration file example:

      # Create required folders
      mkdir -p /etc/arao/surveillance
      mkdir /var/log/arao

      # Copy configuration files
      cd ~/AraoSurveillance
      cp config/config.yml /etc/arao/surveillance
      cp config/logging.yml /etc/arao/surveillance

      # Fix permissions
      chmod 600 /etc/arao/surveillance/config.yml
      chmod 600 /etc/arao/surveillance/logging.yml
      chown camera:camera /etc/arao/surveillance/config.yml
      chown camera:camera /etc/arao/surveillance/logging.yml
      chmod 775 /var/log/arao
      chgrp camera /var/log/arao
      
- Now just edit the configuration file:

      nano /etc/arao/surveillance/config.yml

  
### Usage

Prepare systemd service as user __camera__:

      # Create systemd service under target user
      mkdir -p ~/.config/systemd/user/
      cd ~/.config/systemd/user/
      ln -s ~/AraoSurveillance/conf/arao_surveillance.service
      systemctl --user enable arao_surveillance.service
      systemctl --user start arao_surveillance.service
      systemctl --user status arao_surveillance.service


## ToDo

- Installation script.


## Notes

Any kind of contribution to the project will be welcome.
