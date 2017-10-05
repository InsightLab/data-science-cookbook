# -*- mode: ruby -*-
# vi: set ft=ruby :
# **************************************************************************
# Add specific configuration for running IPython notebooks on a Spark VM
# **************************************************************************

# --------------------------------------------------------------------------
# Variables defining the configuration of Spark & notebook 
# Modify as needed

# RAM memory used for the VM, in MB
vm_memory = '2048'
# Number of CPU cores assigned to the VM
vm_cpus = '1'

# Username that will run all spark processes.
# If remote (yarn) mode is ever going to be used, it is advisable to change it
# to a recognizable unique name, so that it is easily identified in the logs
vm_username = 'vmuser'

# The virtual machine exports the port where the notebook process by forwarding
# it to this port of the local machine
# So to access the notebook server, you point to http://localhost:<port>
port_ipython = 8008

# Note there is an additional port exported: the Spark UI driver is forwarded 
# to port 4040

# This defines the Spark notebook processing mode. There are three choices
# available: "local", "yarn", "standalone"
# It can be changed at runtime by executing inside the virtual machine, as 
# root user, "service notebook set-mode <mode>"
spark_mode = 'local'

# -----------------
# These 3 options are used only when running non-local tasks. They define
# the access points for the remote cluster.
# They can also be modified at runtime by executing inside the virtual
# machine: "sudo service notebook set-addr <A> <B> <C>"
# **IMPORTANT**: If remote mode is to be used, the virtual machine needs
# a network interface in bridge mode. In that case Uncomment the relevant
# lines in the networking section below

# [A] The location of the cluster master (the YARN Resource Manager in Yarn 
# mode, or the Spark master in standalone mode)
spark_master = 'samson02.hi.inet'
# [B] The host running the HDFS namenode
spark_namenode = 'samson01.hi.inet'
# [C] The location of the Spark History Server
spark_history_server = 'samson03.hi.inet:18080'
# ------------------


# --------------------------------------------------------------------------
# Variables defining the Spark installation in the base box. 
# Don't change these

# The place where Spark is deployed inside the local machine
spark_basedir = '/opt/spark'


# --------------------------------------------------------------------------
# Some variables that affect Vagrant execution

# Check the command requested -- if ssh we'll change the login user
vagrant_command = ARGV[0]

# Conditionally activate some provision sections
provision_run_rs  = ENV['PROVISION_RSTUDIO'] == '1' || \
        (vagrant_command == 'provision' && ARGV.include?('20.rstudio'))
provision_run_nbc = (ENV['PROVISION_NBC'] == '1') || \
        (vagrant_command == 'provision' && ARGV.include?('21.nbc'))
provision_run_ai  = ENV['PROVISION_AI'] == '1' || \
        (vagrant_command == 'provision' && ARGV.include?('22.ai'))
#provision_run_ai = true


# --------------------------------------------------------------------------
# Vagrant configuration

# The "2" in Vagrant.configure sets the configuration version
Vagrant.configure(2) do |config|

  # This is to avoid Vagrant inserting a new SSH key, insetad of the 
  # default one (perhaps because the box will be later packaged)
  config.ssh.insert_key = false

  # Use our custom username, instead of the default "vagrant"
  if vagrant_command == "ssh"
      config.ssh.username = vm_username
  end
  config.ssh.username = "vagrant"


  config.vm.define "vm-spark-nb64" do |vgrspark|
  	config.vm.boot_timeout = 600
    #config.name = "vgr-pyspark"

    # The base box we are using. As fetched from ATLAS
    vgrspark.vm.box_version = "= 0"
    vgrspark.vm.box = "data-science"

    # Alternative place: UAM internal
    #vgrspark.vm.box = "uam/spark-base64"
    #vgrspark.vm.box_url = "http://svrbigdata.ii.uam.es/vm/uam-spark-base64.json"
    # Alternative place: TID internal or local box
    #vgrspark.vm.box = "tid/spark-base64"
    #vgrspark.vm.box_url = "http://artifactory.hi.inet/artifactory/vagrant-machinelearning/tid-spark-base64.json"
    #vgrspark.vm.box_url = "file:///almacen/VM/VagrantBox/spark-base64-LOCAL.json"

    # Disable automatic box update checking. If you disable this, then
    # boxes will only be checked for updates when the user runs
    # `vagrant box outdated`. This is not recommended.
    # vgrspark.vm.box_check_update = false

    # Deactivate the usual synced folder and use instead a local subdirectory
    vgrspark.vm.synced_folder ".", "/vagrant", disabled: true
    vgrspark.vm.synced_folder "vmfiles", "/vagrant", 
      mount_options: ["dmode=775","fmode=664"],
      disabled: false
    #owner: vm_username
    #auto_mount: false
  
    # Customize the virtual machine: set hostname & allocated RAM
    vgrspark.vm.hostname = "vm-ipnb-spark"
    vgrspark.vm.provider :virtualbox do |vb|
      # Set the hostname in VirtualBox
      vb.name = vgrspark.vm.hostname.to_s
      # Customize the amount of memory on the VM
      vb.memory = vm_memory
      # Set the number of CPUs
      vb.cpus = vm_cpus
      # Display the VirtualBox GUI when booting the machine
      #vb.gui = true
    end

    # **********************************************************************
    # Networking

    # ---- NAT interface ----
    # NAT port forwarding
    vgrspark.vm.network :forwarded_port, 
     guest: port_ipython,
     host: port_ipython                  # Notebook UI
    # Spark driver UI
    vgrspark.vm.network :forwarded_port, host: 4040, guest: 4040, 
     auto_correct: true
    # Spark driver UI for the 2nd application (e.g. a command-line job)
    vgrspark.vm.network :forwarded_port, host: 4041, guest: 4041,
     auto_correct: true

    # RStudio server
    # =====> uncomment if using RStudio
    #vgrspark.vm.network :forwarded_port, host: 8787, guest: 8787

    # In case we want to fix Spark ports
    #vgrspark.vm.network :forwarded_port, host: 9234, guest: 9234
    #vgrspark.vm.network :forwarded_port, host: 9235, guest: 9235
    #vgrspark.vm.network :forwarded_port, host: 9236, guest: 9236
    #vgrspark.vm.network :forwarded_port, host: 9237, guest: 9237
    #vgrspark.vm.network :forwarded_port, host: 9238, guest: 9238

    # ---- bridged interface ----
    # Declare a public network
    # This enables the machine to be connected from outside, which is a
    # must for a Spark driver [it needs SPARK_LOCAL_IP to be set to 
    # the outside-visible interface].
    # =====> Uncomment the following two lines to enable bridge mode:
    #vgrspark.vm.network "public_network",
    #type: "dhcp"

    # ===> if the host has more than one interface, we can set which one to use
    #bridge: "wlan0"
    # ===> we can also set the MAC address we will send to the DHCP server
    #:mac => "08002710A7ED"


    # ---- private interface ----
    # Create a private network, which allows host-only access to the machine
    # using a specific IP.
    #vgrspark.vm.network "private_network", ip: "192.72.33.10"


    vgrspark.vm.post_up_message = "**** The Vagrant Spark-Notebook machine is up. Connect to http://localhost:" + port_ipython.to_s


    # **********************************************************************
    # Provisioning: install Spark configuration files and startup scripts

    # .........................................
    # Create the user to run Spark jobs (esp. notebook processes)
    vgrspark.vm.provision "01.nbuser",
    type: "shell", 
    privileged: true,
    args: [ vm_username ],
    inline: <<-SHELL
      id "$1" >/dev/null 2>&1 || useradd -c 'User for Spark Notebook' -m -G vagrant "$1"
      su -l "$1" <<-EOF
mkdir bin tmp .ssh 2>/dev/null
chmod 700 .ssh
rm -f bin/{python2.7,pip,ipython}
ln -s /opt/ipnb/bin/ext/{python2.7,pip,ipython,jupyter} /home/$1/bin
test -d .jupyter || mkdir .jupyter
test -h IPNB || { rm -f IPNB; ln -s /vagrant/IPNB/ IPNB; }
echo "export PYSPARK_DRIVER_PYTHON=ipython" >> .bash_profile
echo "export THEANORC=/etc/theanorc:~/.theanorc" >> .bashrc
EOF
      # Install the vagrant public key so that we can ssh to this account
      cp -p /home/vagrant/.ssh/authorized_keys /home/$1/.ssh/authorized_keys
      chown $1.$1 /home/$1/.ssh/authorized_keys
    SHELL

    # Mount the shared folder with the new created user, so that it can write
    # ---> don't, instead we add the user to the vagrant group and mount the 
    #      shared folder with group permissions
#    vgrspark.vm.provision "02.mount",
#    type: "shell",
#    privileged: true,
#    keep_color: true,
#    args: [ vm_username ],
#    inline: <<-SHELL
#umount /vagrant
#mount -t vboxsf -o uid=$(id -u $1),gid=$(id -g $1) vagrant /vagrant
#SHELL

    # .........................................
    # Create the IPython Notebook profile ready to run Spark jobs
    # and install all kernels: Pyspark, Toree (Scala), IRKernel, and extensions
    # Prepared for IPython 4 (so that we configure as a Jupyter app)
    vgrspark.vm.provision "03.nbkernels",
    type: "shell", 
    privileged: true,
    keep_color: true,    
    args: [ vm_username, port_ipython, spark_basedir ],
    inline: <<-SHELL
     # --------------------- Create the Jupyter config
     echo "Creating Jupyter config"
     su -l "$1" -c "cat <<-EOF > /home/$1/.jupyter/jupyter_notebook_config.py
c = get_config()
# define server
c.NotebookApp.ip = '*'
c.NotebookApp.port = $2
c.NotebookApp.open_browser = False
c.NotebookApp.log_level = 'INFO'
c.NotebookApp.notebook_dir = u'/home/$1/IPNB'  
# Preload matplotlib
c.IPKernelApp.matplotlib = 'inline'
EOF
"
     KDIR=/home/$1/.local/share/jupyter/kernels

     # --------------------- Install the Pyspark kernel
     echo "Installing Pyspark kernel"
     KERNEL_NAME=pyspark
     su -l "$1" <<-EOF
mkdir -p "${KDIR}/${KERNEL_NAME}"
cat <<KERNEL > "${KDIR}/${KERNEL_NAME}/kernel.json"
{
    "display_name": "Pyspark (Py 2)",
    "language_info": { "name": "python",
                       "codemirror_mode": { "name": "ipython", "version": 2 }
                     },
    "argv": [
	"/opt/ipnb/bin/ext/pyspark-ipnb",
	"-m", "ipykernel",
	"-f", "{connection_file}"
    ],
    "env": {
        "SPARK_HOME": "/opt/spark/current"
    }
}
KERNEL
# Copy Pyspark kernel logo
cp -p $3/kernel-icons/pyspark-icon-64x64.png $KDIR/$KERNEL_NAME/logo-64x64.png
cp -p $3/kernel-icons/pyspark-icon-32x32.png $KDIR/$KERNEL_NAME/logo-32x32.png
EOF

     # --------------------- Install the Toree Spark kernel
     echo "Installing Toree (Scala) kernel ..."
     KERNEL_NAME='spark'
     KERNEL_DIR="${KDIR}/${KERNEL_NAME}_scala"
     su -l "$1" <<-EOF
/opt/ipnb/bin/ext/jupyter toree install --user --spark_home="$3/current" \
   --kernel_name="$KERNEL_NAME" \
   --spark_opts='--master=local[2] \
      --driver-java-options=-Xms1024M --driver-java-options=-Xmx2048M \
      --driver-java-options=-Dlog4j.logLevel=info'
sed -i 's/"spark - Scala"/"Spark (Scala 2.10)"/' "${KERNEL_DIR}/kernel.json"
# Copy Scala kernel logos
cp -p $3/kernel-icons/scala-spark-icon-64x64.png "${KERNEL_DIR}/logo-64x64.png"
cp -p $3/kernel-icons/scala-spark-icon-32x32.png "${KERNEL_DIR}/logo-32x32.png"
EOF

     # --------------------- Install the IRkernel
     echo "Installing IRkernel ..."
     su -l "$1" <<-EOF
PATH=/opt/ipnb/bin:$PATH LD_LIBRARY_PATH=/opt/rh/python27/root/usr/lib64 Rscript -e 'IRkernel::installspec()'
EOF

     # --------------------- Install the notebook extensions
     echo "Installing notebook extensions"
     su -l "$1" <<-EOF
python2.7 -c 'from notebook.services.config import ConfigManager; ConfigManager().update("notebook", {"load_extensions": {"toc": True, "toggle-headers": True, "search-replace": True, "python-markdown": True }})'
     ln -fs /opt/ipnb/share/jupyter/pre_pymarkdown.py /opt/ipnb/lib/python2.7/site-packages
EOF

     # --------------------- Put the custom Jupyter icon in place
     cd /opt/ipnb/lib/python2.7/site-packages/notebook/static/base/images
     mv favicon.ico favicon-orig.ico
     ln -s favicon-custom.ico favicon.ico

    SHELL

    # .........................................
    # Install the Notebook startup script & configure it
    # Configure Spark execution mode & remote access if defined
    vgrspark.vm.provision "04.nbconfig",
    type: "shell", 
    privileged: true,
    keep_color: true,    
    args: [ spark_basedir, vm_username, spark_mode,
            spark_master, spark_namenode, spark_history_server ],
    inline: <<-SHELL
     # Link the IPython notebook startup script, and set it up for starting
     rm -f /etc/init.d/notebook
     chmod 775 /opt/ipnb/bin/ext/jupyter-notebook-mgr
     ln -s /opt/ipnb/bin/ext/jupyter-notebook-mgr /etc/init.d/notebook
     chkconfig --add notebook

     # Create the config for IPython notebook
     cat <<-EOF > /etc/sysconfig/jupyter-notebook
NOTEBOOK_USER="$2"
NOTEBOOK_SCRIPT="/opt/ipnb/bin/ext/jupyter-notebook"
EOF

     # Configure remote addresses
     if [ "$4" ]; then
       service notebook set-addr yarn "$4" "$5" "$6"
       service notebook set-addr standalone "$4" "$5" "$6"
     fi 

     # Set the name of the initially active config
     echo "Configuring Spark mode as: $3"
     service notebook set-mode "$3"
  SHELL


    # .........................................
    # Create a subdirectory in the shared folder linked to the 
    # default name of the Hive warehouse directory
    vgrspark.vm.provision "05.hive.warehouse",
    type: "shell",
    keep_color: true,
    privileged: true,
    inline: <<-SHELL
      mkdir -p /user/hive
      ln -s /vagrant/warehouse /user/hive/warehouse
    SHELL

    # .........................................
    # Install the neuralnet R package
    # vgrspark.vm.provision "10.r.neuralnet",
    # type: "shell",
    # keep_color: true,
    # privileged: true,
    # inline: <<-SHELL
    #  echo "Installing R packages"
    #  for pkg in '"neuralnet"'
    #  do
    #      echo -e "\nInstalling R packages: $pkg"
    #      Rscript -e "install.packages(c($pkg),dependencies=TRUE,repos=c('http://ftp.cixug.es/CRAN/','http://cran.es.r-project.org/'),quiet=FALSE)"
    #  done
    # SHELL

    # .........................................
    # Install RStudio server
    # Do it only if explicitly requested (either by environment variable 
    # PROVISION_RSTUDIO when creating or by --provision-with 20.rstudio) 
    # *** Don't forget to also uncomment forwarding for port 8787!
    if (provision_run_rs)
      vgrspark.vm.provision "20.rstudio",
      type: "shell",
      keep_color: true,
      privileged: true,
      args: [ vm_username ],
      inline: <<-SHELL
        echo "Downloading & installing RStudio Server"
        # Download & install the RPM for RStudio server
        PKG=rstudio-server-rhel-0.99.903-x86_64.rpm
        wget --no-verbose https://download2.rstudio.org/$PKG
        yum install -y --nogpgcheck $PKG
        rm $PKG
        # Define the directory for the user library
        echo "r-libs-user=~/.Rlibrary" >> /etc/rstudio/rsession.conf
        # Create a link to the host-mounted R subdirectory
        sudo -i -u "$1" bash -c "rm -f R; ln -s /vagrant/R/ R"
        # Set the password for the user, so that it can log in in RStudio
        echo "$1" | passwd --stdin "$1"
        # Send message
        echo "RStudio Server should be accessed at http://localhost:8787"
        echo "(if not, check in Vagrantfile that port 8787 has been forwarded)"
      SHELL
    end

    # .........................................
    # Install the necessary components for nbconvert to work.
    # Do it only if explicitly requested (either by environment variable 
    # PROVISION_NBC when creating or by --provision-with 21.nbc) 
    if (provision_run_nbc)
      vgrspark.vm.provision "21.nbc",
      type: "shell",
      privileged: true,
      keep_color: true,
      args: [ vm_username ],
      inline: <<-SHELL
          echo "Installing nbconvert requisites"
          yum install -y pandoc inkscape
          sudo -i -u vagrant pip install pandoc
          DIR=$(kpsewhich -var-value TEXMFLOCAL)
          mkdir -p $DIR
          cd $DIR
          for p in collectbox adjustbox; do
            wget --no-verbose http://mirrors.ctan.org/install/macros/latex/contrib/$p.tds.zip
            unzip -o $p.tds.zip
            rm $p.tds.zip
          done
          texhash
      SHELL
    end

    # .........................................
    # Install the additional packages for the AI course
    # Do it only if explicitly requested (either by environment variable 
    # PROVISION_AI when creating or by --provision-with 22.ai) 
    if (provision_run_ai)
      vgrspark.vm.provision "22.ai",
      type: "shell",
      privileged: true,
      keep_color: true,
      args: [ vm_username ],
      inline: <<-SHELL
        echo "Installing packages for AI course"
        yum -y install python27-tkinter
        su -l "vagrant" <<-EOF
         pip install nltk graphviz
         pip install aimlbotkernel
         pip install sparqlkernel
EOF
        su -l "$1" <<-EOF
         echo "Installing AIML-BOT & SPARQL kernels"
         jupyter aimlbotkernel install --user
         jupyter sparqlkernel install --user --logdir /var/log/ipnb
EOF

      SHELL
    end


    # .........................................
    # Start Jupyter Notebook
    # Note: this one we run it every time the machine boots, since during 
    # the VM boot sequence the startup script is executed before vagrant has 
    # mounted the shared folder, and hence it fails. 
    # Running it as a provisioning makes it run *after* vagrant mounts, so 
    # this way it works.
    # [An alternative would be to force mounting on startup, by adding the
    # vboxsf mount point to /etc/fstab during provisioning]
    vgrspark.vm.provision "50.nbstart", 
      type: "shell", 
      run: "always",
      privileged: true,
      keep_color: true,    
      inline: "/etc/init.d/notebook start"


  end # config.vm.define

end
