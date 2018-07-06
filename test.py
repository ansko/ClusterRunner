import paramiko

# settings, keep them private!
from settings_kiae_me import host, user, pwd, key


def copy_to_server(paramiko_ssh_client_connected, local_path, remote_path):
    sftp = paramiko_ssh_client_connected.open_sftp()
    sftp.put(local_path, remote_path)
    sftp.close()


def set_task_in_a_queue(task_string):
    local_path = '/home/anton/AspALL/Projects/FEM_RELEASE/readme'
    remote_path = '/s/ls2/users/antonsk/FEM/1.geo'
    # establish connectoin
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=user, password=pwd, key_filename=key)
    # executing commands
    commands_list = '; '.join([
        'cd /s/ls2/users/antonsk/FEM',
        #'pwd',
        'export LD_LIBRARY_PATH=libs',
        task_string
    ])
    #stdin, stdout, stderr = ssh.exec_command(commands_list)
    #print(stdout.readlines())
    # closing connection
    ssh.close()


def get_server_state():
    pass


def single_loop():
    # create structure and .geo file as '1.geo'
    # copy it to the cluster
    # run task 'sbatch fem_gen.sh'
    # wait until it completes
    # if succeed rename 'generated.vol into out.mesh' and
    #     run task 'sbatch fem_process.sh'
    # wait until it completes
    # x3:
    #     if succeed create 'input.txt' and
    #         run task 'sbatch fem_3_anton.sh'
    # wait until it completes
    # copy results
    return 0


single_loop()
