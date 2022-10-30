- name: 'variable for host'
  hosts: all
  vars:
         x: 10
         y: 14
  tasks:
  - name: 'debug'
    debug:
        msg: "this is test print"
  - name: 'print variable'
    debug: 
        var: x
  - name: 'print variable with msg'
    debug:
       msg: "this os my data from {{y}} variable hello"  
