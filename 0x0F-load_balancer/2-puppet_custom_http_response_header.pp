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
  after  =>  'location / {',
  line   =>  '\tadd_header X-Served-By $HOSTNAME;',
}
