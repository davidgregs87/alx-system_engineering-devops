# Puppet script to authenticate without using a password

file { '/etc/ssh/ssh_config':
  path     =>  '/usr/bin',
  command  =>  'echo "IdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config; echo "PasswordAuthentication no" >> /etc/ssh/ssh_config',
}
