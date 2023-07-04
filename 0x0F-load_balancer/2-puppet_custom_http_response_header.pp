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
  after  =>  '	try_files $uri $ur1/ =404;',
  line   =>  'add_header X-Served-By $HOSTNAME;',
}
