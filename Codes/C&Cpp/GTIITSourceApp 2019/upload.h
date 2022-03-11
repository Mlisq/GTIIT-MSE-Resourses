#ifndef UPLOAD_H
#define UPLOAD_H

#include <QObject>
#include "QSsh/sshconnection.h"
#include "QSsh/sshremoteprocessrunner.h"
#include "QSsh/sshdirecttcpiptunnel.h"
#include "QSsh/sshconnectionmanager.h"
#include "QSsh/sftpchannel.h"

using namespace QSsh;

class Upload : public QObject
{
    Q_OBJECT
public:
    explicit Upload(QObject *parent = nullptr);
    ~Upload();
    void setPath(QString p,QString fn);
signals:
    void uploadCompleted();
    void pathinitializedFailed();
private:
     SshConnection *c;
     SftpChannel::Ptr cn;
     QSharedPointer<SshRemoteProcess> s;
     QString path;
     QString fileName;
private slots:
    void handleChannelInitialized();
    void afterConnection();
};

#endif // UPLOAD_H
