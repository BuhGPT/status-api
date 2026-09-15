// BuhGPT Status — check the ESF system before sending. Data: BuhGPT Статус — buhgpt.kz/status
// 1C:Enterprise script, English syntax.

Function BuhGPTSystemStatus(SystemId = "esf", Lang = "kk") Export

	Try
		Connection = New HTTPConnection("buhgpt.kz", 443, , , , 10, New OpenSSLSecureConnection);
		Request = New HTTPRequest("/status/api/pulse/v1/context?service=" + SystemId + "&lang=" + Lang);
		Response = Connection.Get(Request);
		If Response.StatusCode <> 200 Then
			Return Undefined;
		EndIf;
		Reader = New JSONReader;
		Reader.SetString(Response.GetBodyAsString("UTF-8"));
		Return ReadJSON(Reader);
	Except
		Return Undefined;
	EndTry;

EndFunction

Procedure ShowESFStatus() Export

	State = BuhGPTSystemStatus("esf");
	If State = Undefined Then
		Return;
	EndIf;
	Message(State.service_name + ": " + State.status_label + ". " + State.advice);
	Message(State.attribution);

EndProcedure
