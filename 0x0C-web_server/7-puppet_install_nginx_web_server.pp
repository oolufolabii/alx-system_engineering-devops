# Puppet manifest to install nginx

package { 'nginx':
  ensure => installed,
}

file_line { 'aaaaa':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}

file { 'The home page':
  ensure  => file,
  path    => '/var/www/html/index.html',
  mode    => '0744',
  owner   => 'www-data',
  content => "Hello World!\n"
}
