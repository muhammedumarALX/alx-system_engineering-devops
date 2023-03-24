# kills a process name killmenow

exec{ 'pkill killmenow':
  command => '/usr/bin/pkill killmenow',
  onlyif  => '/bin/pgrep killmenow',
}
