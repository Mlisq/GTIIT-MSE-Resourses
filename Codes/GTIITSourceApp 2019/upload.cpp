#include "upload.h"

Upload::Upload(QObject *parent) : QObject(parent)
{
    SshConnectionParameters p;

    p.host = "106.53.89.68";
    p.userName = "admin";
    p.password = "]'/[;.pl,";
    p.timeout = 500;
    p.port = 22;
    p.authenticationType = QSsh::SshConnectionParameters::AuthenticationTypePassword;
    if(c==nullptr)
    {
        c = new SshConnection(p);
        connect(c,&SshConnection::connected,this,&Upload::afterConnection);
    }
    c->connectToHost();
}

Upload::~Upload()
{
    delete c;
}

void Upload::afterConnection()
{
    cn = c->createSftpChannel();
    s = c->createRemoteShell();
    connect(cn.data(), SIGNAL(initialized()), this, SLOT(handleChannelInitialized()));
    cn->initialize();
}

void Upload::handleChannelInitialized()
{
    if(path == nullptr || fileName == nullptr)
        emit pathinitializedFailed();
    else
    {
        cn->uploadFile(path,"../..//var/www/html/upload/"+fileName,SftpOverwriteExisting);
        s->start();
        emit uploadCompleted();
    }
}

void Upload::setPath(QString p,QString fn)
{
    path = p;
    fileName = fn;
}
