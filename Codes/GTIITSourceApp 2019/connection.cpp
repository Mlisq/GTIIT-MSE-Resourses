#include "connection.h"
#include <QDebug>
#include <QWidget>

Connection::Connection(QObject *parent) : QObject(parent)
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
        connect(c,&SshConnection::connected,this,&Connection::afterConnection);
    }
    c->connectToHost();
}

void Connection::initStringList()
{
    /*QStringList l;      //得到的StringList
    l << "ME" << "ME/FIRST" << "ME/FIRST/SCOUND" ;
    l << "CE" << "CE/FIRST" << "CE/FIRST/SCOUND" ;*/

    QStringList mainlist;

    for (int i = 0 ; i < ll.size()-1 ; i++)
    {
        if(!ll.at(i).contains("/"))
            mainlist.append(ll.at(i));
    }

    QStringList templist;

    for(int i = 0; i < mainlist.size(); i ++)
    {
        templist.append(mainlist.at(i));
        for(int j = 0; j < ll.size(); j ++)
        {
            if(!ll.at(j).contains("/") || ll.at(j) == mainlist.at(i))
                continue;
            if(ll.at(j).contains(mainlist.at(i)))
            {
                templist.append(ll.at(j));
            }
        }
        list.append(templist);
        templist.clear();
    }
    //list.removeFirst();
}

QList<QStringList> Connection::getList()
{
    return list;
}

void Connection::afterConnection()
{
    s = c->createRemoteShell();
    connect(s.data(),SIGNAL(started()), SLOT(afterShellStarted()));
    connect(s.data(),SIGNAL(readyReadStandardOutput()), SLOT(afterReadOutput()));
    s.data()->start();
}

void Connection::afterShellStarted()
{
    s.data()->write(QString("cd ../../var/www/html/gtsource\nfind . -print0 | xargs -0 stat --printf=\"%N\n\"\n").toLatin1().data());
}

void Connection::afterReadOutput()
{
    QString str = QString(s.data()->readAllStandardOutput());
    str.replace(2,"");
    str.replace("‘","");
    str.replace("’","");
    str.replace("\r","");
    str.replace("\n","");
    str.replace("\u001B[0m\u001B[01;34m","");
    str.replace("\u001B[0m  \u001B[01;34m", "");
    str.replace("[admin@VM_0_14_centos gtsource]$ ","");
    str.replace("var/www/html/gtsourcefind . -print0 | xargs -0 stat --printf=\"%N\"","");
    str.replace("var/www/html/gtsourcefind . -print0 | xargs -0 stat --printf=\"%N> \"","");
    ll = str.split("./");
    for(int i=0; i < ll.size()-1;i++)
    {
        //if(ll.at(i) == "") ll.removeAt(i);
        if(ll.at(i).endsWith("."))
        {
            ll.replace(i,"");
        }
    }
    ll.removeFirst();

    if(!ll.isEmpty())
    {
        initStringList();
        emit Done();
    }else
        qDebug() << "reading error";
}

void Connection::refresh()
{
    list.clear();
    ll.clear();
    afterShellStarted();
}

Connection::~Connection()
{
    delete c;
}
