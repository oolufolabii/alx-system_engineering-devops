# Fixes a wordpress site running on apache2
exec { 'fix-wordpress':
  command => 'bash -c "sed -i s/class-wp-locale.phpp/class-wp-locale.php/ \
/var/www/html/wp-settings.php; sudo service apache2 restart"',
  path    => '/usr/bin:/usr/sbin:/bin'
}
