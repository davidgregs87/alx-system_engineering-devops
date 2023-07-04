# Configure nginx to add custom header X-Served-By to new server

package { 'nignx':
  ensure  =>  installed,
}

file { '/var/www/html/index.html':
  content =>  'Hello World!',
}

service { 'nginx':
  ensure  =>  running,
  require =>  package['nginx'],
}

file_line { 'server_config':
  ensure =>  present,
  path   =>  '/etc/nginx/sites-available/default',
  line               => '  try_files $uri $uri =404;',
  after              => '  try_files $uri $uri =404;',
  match              => '^.*try_files \$uri \$uri =404;.*$',
  append_on_no_match => false,
  content            => "    add_header X-Served-By \$HOSTNAME;\n",
}
