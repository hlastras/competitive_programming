defmodule Master do
  use GenServer

  alias Slave

  def start_link() do
    GenServer.start_link(__MODULE__, nil)
  end

  def init(nil) do
    send(self(), :start_child)
    {:ok, []}
  end

  def handle_info(:start_child, children_list) do
    {:ok, slave} = Slave.start_link(self())
    {:noreply,  children_list ++ [slave]}
  end
end
